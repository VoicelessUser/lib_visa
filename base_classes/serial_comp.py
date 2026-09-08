import serial
import time
import logging
import random

TEST_PORT = 'test'
TEST_FLOAT_PORT = 'test_float'
TEST_LIST_PORT = 'test_list'
TEST_PORTS = (TEST_PORT, TEST_FLOAT_PORT, TEST_LIST_PORT)


class SerialComp:
    def __init__(self, port: str = '', baudrate: int = 115200, timeout: float = 1.0):
        self.logger = logging.getLogger("hw")
        self._port = port
        self._baudrate = baudrate
        self._timeout = timeout
        self._connection: serial.Serial | None = None

    def connect(self):
        if self._port in TEST_PORTS:
            self.logger.info(
                f"Test mode ({self._port}) for {self.__class__.__name__}"
            )
            return
        try:
            self._connection = serial.Serial(
                port=self._port,
                baudrate=self._baudrate,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=self._timeout,
                rtscts=True,
            )
            time.sleep(0.1)
            self._connection.reset_input_buffer()
            self.logger.info(f"Connected to {self.__class__.__name__} on {self._port}")
        except Exception as e:
            self.logger.error(f"Failed to connect: {e}")
            self._connection = None

    def disconnect(self):
        if self._connection and self._connection.is_open:
            try:
                self._connection.close()
                self.logger.info(f'Disconnected from {self.__class__.__name__}')
            except Exception as e:
                self.logger.error(f"Error during disconnect: {e}")
            self._connection = None
        return self

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()


    def _ask_parameter(self, command: str, max_attempts: int = 2, delay: float = 0.2) -> str:
        """Отправляет запрос и ждёт ответ."""
        if self._port == TEST_PORT:
            return str(int(time.time()))
        if self._port == TEST_FLOAT_PORT:
            return f'{2.5 + random.uniform(-0.1, 0.1)}'
        if self._port == TEST_LIST_PORT:
            count = random.randint(1, 10)
            return ','.join(str(2.5 + random.uniform(-0.1, 0.1)) for _ in range(count))
        if not self._connection or not self._connection.is_open:
            self.logger.error("Not connected")
            return "Not connected"

        def try_query(com: str) -> str:
            self._send_raw(com)
            answer = self._read_response()
            self.logger.info(f'{self.__class__.__name__}: {com} -> {answer}')
            return answer

        try:
            return try_query(command)
        except Exception as e:
            try:
                for attempt in range(max_attempts):
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
        if not self._connection or not self._connection.is_open:
            self.logger.error("Not connected")
            return False

        try:
            self._send_raw(command)
            self.logger.info(f'{self.__class__.__name__}: {command}')
            return True
        except Exception as e:
            self.logger.error(f"Failed to write command {command}: {e}")
            return False

    def _send_raw(self, command: str):
        """Отправляет сырые байты через serial."""
        if not self._connection or not self._connection.is_open:
            raise ConnectionError("Not connected")
        self._connection.write(f"{command}\n".encode())
        self._connection.flush()

    def _read_response(self, timeout: float = None) -> str:
        """Читает ответ от устройства."""
        if not self._connection or not self._connection.is_open:
            raise ConnectionError("Not connected")
        
        timeout = timeout or self._timeout
        response_lines = []
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self._connection.in_waiting:
                line = self._connection.readline().decode().strip()
                if line:
                    response_lines.append(line)
                    if not self._connection.in_waiting:
                        break
        time.sleep(0.1)
        return "\n".join(response_lines) if response_lines else ""

    def _try_new_comm(self, command: str, get_answer: bool):
        """Пробует установить соединение, выполнить команду и отключиться."""
        with self:
            if get_answer:
                response = self._ask_parameter(command)
                self.logger.info(f'{self.__class__.__name__}: {command} -> {response}')
            else:
                self._set_parameter(command)
                self.logger.info(f'{self.__class__.__name__}: {command}')