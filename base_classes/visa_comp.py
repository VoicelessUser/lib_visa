import pyvisa
import time
import yaml
import logging
import platform

from pyvisa import constants

class VisaComp:
    # Таймаут по умолчанию (мс). Наследники могут переопределить.
    _default_timeout = 2000

    def __init__(self, port: str = ''):
        self.logger = logging.getLogger("hw")
        self._port = port
        self._connection = None
        self._rm = None
        self._timeout = self._default_timeout
        self._max_try_query = 2
        self._max_try_connect = 3
        self._reconnect_delay = 0.5

    def _get_resource_manager(self):
        """Автовыбор VISA-бэкенда с кэшированием ResourceManager.

        ResourceManager создаётся один раз на объект: создание нового RM на
        каждый запрос переоткрывает USB-ресурс и может «уронить» прибор с
        шины (VI_ERROR_RSRC_NFOUND).
        """
        if self._rm is not None:
            return self._rm

        is_arm_linux = (
            platform.system() == 'Linux'
            and platform.machine().startswith(('arm', 'aarch'))
        )

        if is_arm_linux:
            try:
                self._rm = pyvisa.ResourceManager('@py')
                self.logger.info("Using pyvisa-py backend (ARM Linux)")
                return self._rm
            except Exception as e:
                self.logger.warning(f"pyvisa-py not available on ARM: {e}")

        try:
            self._rm = pyvisa.ResourceManager()
            self.logger.info(f"Using default VISA backend: {self._rm.visalib}")
            return self._rm
        except Exception as e:
            self.logger.error(f"Default VISA failed: {e}")
            # Финальная попытка — pyvisa-py
            try:
                self._rm = pyvisa.ResourceManager('@py')
                self.logger.info("Using pyvisa-py backend (fallback)")
                return self._rm
            except Exception as e2:
                self.logger.error(f"pyvisa-py also failed: {e2}")
                raise RuntimeError("No VISA backend available") from e2

    def connect(self):
        """Подключается к прибору с повторными попытками (реконнект).

        Если соединение уже открыто — ничего не делает.
        После _max_try_connect неудачных попыток бросает ConnectionError.
        """
        if self._connection:
            return

        last_err = None
        for attempt in range(1, self._max_try_connect + 1):
            try:
                rm = self._get_resource_manager()
                self._connection = rm.open_resource(self._port)
                self._connection.timeout = self._timeout
                self.logger.info(
                    f"Connected to {self.__class__.__name__} on {self._port}"
                )
                return
            except Exception as e:
                last_err = e
                self._connection = None
                self.logger.error(
                    f"Connect attempt {attempt}/{self._max_try_connect} "
                    f"failed: {e}"
                )
                time.sleep(self._reconnect_delay)

        raise ConnectionError(
            f"Could not connect to {self._port}"
        ) from last_err

    def disconnect(self):
        if self._connection:
            try:
                self._connection.close()
                self.logger.info(
                    f'Disconnected from {self.__class__.__name__}'
                )
            except Exception as e:
                self.logger.error(f"Error during disconnect: {e}")
            self._connection = None
        if self._rm is not None:
            try:
                self._rm.close()
            except Exception as e:
                self.logger.error(f"Error closing resource manager: {e}")
            self._rm = None
        return self

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def identify_yourself(self) -> str:
        """Запрашивает идентификатор устройства."""
        return self._ask_parameter("*IDN?")

    def _discard_input_buffer(self) -> None:
        """Сбрасывает входной буфер прибора, не разрывая соединение."""
        if not self._connection:
            return
        try:
            self._connection.flush(
                constants.BufferOperation.discard_read_buffer
            )
        except Exception as e:
            self.logger.warning(f"Failed to flush input buffer: {e}")

    def _ask_parameter(self, command: str, delay: float = 0.2) -> str:
        """Отправляет запрос и ждёт ответ. При обрыве — реконнект и ретрай."""
        if not self._connection:
            try:
                self.connect()
            except Exception as e:
                self.logger.error(f"Not connected, reconnect failed: {e}")
                return "Not connected"

        last_err = None
        for attempt in range(self._max_try_query):
            try:
                answer = self._connection.query(command)
                self.logger.info(
                    f'{self.__class__.__name__}: {command} -> {answer}'
                )
                return answer
            except Exception as e:
                last_err = e
                self.logger.error(
                    f"Query attempt {attempt + 1}/{self._max_try_query} "
                    f"failed: {e}"
                )
                # НЕ переоткрываем ресурс: сбрасываем входной буфер и
                # повторяем запрос в том же соединении. Переоткрытие
                # рвёт USB-сессию и роняет прибор с шины.
                self._discard_input_buffer()
                time.sleep(delay)

        return f"Error: {last_err}"

    def _set_parameter(self, command: str) -> bool:
        """Отправляет команду без ожидания ответа. При обрыве — реконнект."""
        if not self._connection:
            try:
                self.connect()
            except Exception as e:
                self.logger.error(f"Not connected, reconnect failed: {e}")
                return False

        for attempt in range(self._max_try_query):
            try:
                self._connection.write(command)
                self.logger.info(f'{self.__class__.__name__}: {command}')
                return True
            except Exception as e:
                self.logger.error(
                    f"Write attempt {attempt + 1}/{self._max_try_query} "
                    f"failed for {command}: {e}"
                )
                # без переоткрытия ресурса — просто сброс буфера и повтор
                self._discard_input_buffer()
                time.sleep(self._reconnect_delay)
        return False

    def _try_new_comm(self, command: str, get_answer: bool):
        """Пробует установить соединение, выполнить команду и отключиться."""
        with self:
            if get_answer:
                response = self._ask_parameter(command)
                self.logger.info(
                    f'{self.__class__.__name__}: {command} -> {response}'
                )
            else:
                self._set_parameter(command)
                self.logger.info(f'{self.__class__.__name__}: {command}')

if __name__ == '__main__':
    with open('all_ports.yaml', 'r') as f:
        port_dict = yaml.load(f, Loader=yaml.FullLoader)

    device = VisaComp(port_dict['power_supply'])
    with device:
        print(device.identify_yourself())