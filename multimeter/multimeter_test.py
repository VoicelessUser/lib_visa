from .base_multimeter import CommList, Meas, BaseMultimeter
from ..base_classes.visa_comp_test import VisaCompTest, TEST_PORT

multimeter_test_commands = CommList(
    voltage_dc=':TRIG:COUN 1;:MEAS AUTO;:MEAS:VOLT:DC?',
    voltage_ac=':TRIG:COUN 1;:MEAS AUTO;:MEAS:VOLT:AC?',
    current_dc=':TRIG:COUN 1;:MEAS AUTO;:MEAS:CURR:DC?',
    current_ac=':TRIG:COUN 1;:MEAS AUTO;:MEAS:CURR:AC?',
    resistance=':TRIG:COUN 1;:MEAS AUTO;:MEAS:RES?',
    frequency=':TRIG:COUN 1;:MEAS AUTO;:MEAS:FREQ?',
    capacitance=':TRIG:COUN 1;:MEAS AUTO;:MEAS:CAP?',
    continuity=':TRIG:COUN 1;:MEAS AUTO;:MEAS:CONT?',
    diode=':TRIG:COUN 1;:MEAS AUTO;:MEAS:DIOD?',
    temperature=''
)


class MultimeterTest(BaseMultimeter, VisaCompTest):
    """Виртуальный мультиметр для отладки без железа.

    Отвечает на любой запрос timestamp (порт 'test'), команды записи
    логируются. Все измерения доступны как у реального прибора.
    """

    def __init__(self, port: str = TEST_PORT):
        super().__init__(port)
        self._comm_list = multimeter_test_commands
        self.meas = Meas(self, self._comm_list)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)

    with MultimeterTest() as multik:
        print('IDN ->', multik.identify_yourself())
        print('Vdc =', multik.meas.voltage_dc)
        print('R   =', multik.meas.resistance)
