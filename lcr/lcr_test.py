from .base_lcr import LCRCommands, BaseLcrMeter
from ..base_classes.visa_comp_test import VisaCompTest, TEST_PORT


class LcrTest(BaseLcrMeter, VisaCompTest):
    """Виртуальный LCR-метр для отладки без железа.

    Отвечает на любой запрос timestamp (порт 'test'), команды записи
    логируются. Измерение meas возвращает список из одного значения.
    """

    def __init__(self, port: str = TEST_PORT):
        super().__init__(port=port, commands=LCRCommands())


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)

    with LcrTest() as lcr:
        print('IDN ->', lcr.identify_yourself())
        lcr.frequency = 1000
        print('meas =', lcr.meas)
