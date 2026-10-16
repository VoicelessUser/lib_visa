import time
import random

from .visa_comp import VisaComp

# Тестовые адреса портов:
#   'test'       — любой запрос отвечает целым числом (timestamp)
#   'test_float' — случайным float около 2.5
#   'test_list'  — списком случайных float через запятую
TEST_PORT = 'test'
TEST_FLOAT_PORT = 'test_float'
TEST_LIST_PORT = 'test_list'
TEST_PORTS = (TEST_PORT, TEST_FLOAT_PORT, TEST_LIST_PORT)


class VisaCompTest(VisaComp):
    """Виртуальный VISA-прибор для отладки без железа.

    Имитирует ответы прибора:
        'test'       — любой запрос возвращает timestamp (целое число)
        'test_float' — случайный float около 2.5
        'test_list'  — список случайных float через запятой

    Команды записи логируются, но никуда не отправляются.
    """

    def __init__(self, port: str = TEST_PORT):
        super().__init__(port)

    def connect(self):
        if self._port in TEST_PORTS:
            self.logger.info(
                f"Test mode ({self._port}) for {self.__class__.__name__}"
            )
            return
        super().connect()

    def _ask_parameter(self, command: str, delay: float = 0.2) -> str:
        if self._port == TEST_PORT:
            return str(int(time.time()))
        if self._port == TEST_FLOAT_PORT:
            return f'{2.5 + random.uniform(-0.1, 0.1)}'
        if self._port == TEST_LIST_PORT:
            count = random.randint(1, 10)
            return ','.join(
                str(2.5 + random.uniform(-0.1, 0.1)) for _ in range(count)
            )
        return super()._ask_parameter(command, delay)

    def _set_parameter(self, command: str) -> bool:
        if self._port in TEST_PORTS:
            self.logger.info(
                f'{self.__class__.__name__} (test mode): {command}'
            )
            return True
        return super()._set_parameter(command)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)

    with VisaCompTest() as device:
        print('*IDN? ->', device.identify_yourself())

    with VisaCompTest(TEST_FLOAT_PORT) as device:
        print('test_float ->', device._ask_parameter(':MEAS:VOLT?'))

    with VisaCompTest(TEST_LIST_PORT) as device:
        print('test_list ->', device._ask_parameter('TRAC:DATA?'))
