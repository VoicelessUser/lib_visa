import pyvisa
import time
import yaml
import logging
import platform
import random

TEST_PORT = 'test'
TEST_FLOAT_PORT = 'test_float'
TEST_LIST_PORT = 'test_list'
TEST_PORTS = (TEST_PORT, TEST_FLOAT_PORT, TEST_LIST_PORT)


class VisaComp:
    def __init__(self, port: str = ''):
        self.logger = logging.getLogger("hw")
        self._port = port
        self._connection = None
        self._timeout = 2000
        self._max_try_query = 2

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
        if self._port in TEST_PORTS:
            self.logger.info(
                f"Test mode ({self._port}) for {self.__class__.__name__}"
            )
            return
        try:
            rm = self._get_resource_manager()
            self._connection = rm.open_resource(self._port)
            self._connection.timeout = self._timeout
            self.logger.info(
                f"Connected to {self.__class__.__name__} on {self._port}"
            )
        except Exception as e:
            self.logger.error(f"Failed to connect: {e}")
            self._connection = None
            raise

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
        """Отправляет запрос и ждёт ответ."""
        if self._port == TEST_PORT:
            return str(int(time.time()))
        if self._port == TEST_FLOAT_PORT:
            return f'{2.5 +random.uniform(-0.1, 0.1)}'
        if self._port == TEST_LIST_PORT:
            count = random.randint(1, 10)
            return ','.join(str(2.5 + random.uniform(-0.1, 0.1)) for _ in range(count))
        if not self._connection:
            self.logger.error("Not connected")
            return "Not connected"

        def try_query(com: str) -> str:
            answer = self._connection.query(com)
            self.logger.info(
                f'{self.__class__.__name__}: {com} -> {answer}'
            )
            return answer

        try:
            return try_query(command)
        except Exception as e:
            try:
                for attempt in range(self._max_try_query):
                    self.disconnect()
                    time.sleep(delay)
                    self.connect()
                    try:
                        return try_query(command)
                    except Exception as e:
                        self.logger.error(f"Failed to read answer: {e}")
                        time.sleep(delay)
                return f"Error: {e}"
            except Exception as e:
                self.logger.error(f"Error during retry: {e}")
                return f"Error: {e}"

    def _set_parameter(self, command: str) -> bool:
        """Отправляет команду без ожидания ответа."""
        if self._port in TEST_PORTS:
            self.logger.info(
                f'{self.__class__.__name__} (test mode): {command}'
            )
            return True
        if not self._connection:
            self.logger.error("Not connected")
            return False

        try:
            self._connection.write(command)
            self.logger.info(f'{self.__class__.__name__}: {command}')
            return True
        except Exception as e:
            self.logger.error(f"Failed to write command {command}: {e}")
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
