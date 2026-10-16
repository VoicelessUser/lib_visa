import pyvisa
import time
import yaml
import logging
import platform

class VisaComp:
    def __init__(self, port: str = ''):
        self.logger = logging.getLogger("hw")
        self._port = port
        self._connection = None
        self._timeout = 2000
        self._max_try_query = 2
        self._max_try_connect = 3
        self._reconnect_delay = 0.5

    def _get_resource_manager(self):
        """Автовыбор VISA-бэкенда: NI-VISA если есть, иначе pyvisa-py.

        На Raspberry Pi / ARM Linux принудительно используем @py,
        т.к. NI-VISA там не доступен.
        """
        is_arm_linux = (
            platform.system() == 'Linux'
            and platform.machine().startswith(('arm', 'aarch'))
        )

        if is_arm_linux:
            try:
                rm = pyvisa.ResourceManager('@py')
                self.logger.info("Using pyvisa-py backend (ARM Linux)")
                return rm
            except Exception as e:
                self.logger.warning(f"pyvisa-py not available on ARM: {e}")

        try:
            rm = pyvisa.ResourceManager()
            self.logger.info(f"Using default VISA backend: {rm.visalib}")
            return rm
        except Exception as e:
            self.logger.error(f"Default VISA failed: {e}")
            # Финальная попытка — pyvisa-py
            try:
                rm = pyvisa.ResourceManager('@py')
                self.logger.info("Using pyvisa-py backend (fallback)")
                return rm
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
        return self

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def identify_yourself(self) -> str:
        """Запрашивает идентификатор устройства."""
        return self._ask_parameter("*IDN?")

    def _ask_parameter(self, command: str, delay: float = 0.2) -> str:
        """Отправляет запрос и ждёт ответ. При обрыве — реконнект и ретрай."""
        if not self._connection:
            try:
                self.connect()
            except Exception as e:
                self.logger.error(f"Not connected, reconnect failed: {e}")
                return "Not connected"

        def try_query(com: str) -> str:
            answer = self._connection.query(com)
            self.logger.info(
                f'{self.__class__.__name__}: {com} -> {answer}'
            )
            return answer

        last_err = None
        for attempt in range(self._max_try_query):
            try:
                return try_query(command)
            except Exception as e:
                last_err = e
                self.logger.error(
                    f"Query attempt {attempt + 1}/{self._max_try_query} "
                    f"failed: {e}"
                )
                # реконнект и повторный запрос
                try:
                    self.disconnect()
                    time.sleep(delay)
                    self.connect()
                except Exception as e_conn:
                    last_err = e_conn
                    self.logger.error(f"Reconnect failed: {e_conn}")
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

        try:
            self._connection.write(command)
            self.logger.info(f'{self.__class__.__name__}: {command}')
            return True
        except Exception as e:
            self.logger.error(f"Failed to write command {command}: {e}")
            # одна попытка реконнекта и повторной отправки
            try:
                self.disconnect()
                time.sleep(self._reconnect_delay)
                self.connect()
                self._connection.write(command)
                self.logger.info(
                    f'{self.__class__.__name__} (after reconnect): {command}'
                )
                return True
            except Exception as e2:
                self.logger.error(
                    f"Failed to write command {command} after reconnect: {e2}"
                )
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