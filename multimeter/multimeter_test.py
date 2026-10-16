from .base_multimeter import CommList, Measurement, BaseMultimeter
from ..base_classes.visa_comp_test import VisaCompTest, TEST_PORT

multimeter_test_commands = CommList(
    setup=(':TRIG:COUN 1;:MEAS AUTO',),
    voltage_dc=Measurement(read=':MEAS:VOLT:DC?'),
    voltage_ac=Measurement(read=':MEAS:VOLT:AC?'),
    current_dc=Measurement(read=':MEAS:CURR:DC?'),
    current_ac=Measurement(read=':MEAS:CURR:AC?'),
    resistance=Measurement(read=':MEAS:RES?'),
    frequency=Measurement(read=':MEAS:FREQ?'),
    capacitance=Measurement(read=':MEAS:CAP?'),
    continuity=Measurement(read=':MEAS:CONT?'),
    diode=Measurement(read=':MEAS:DIOD?'),
    temperature=Measurement()
)


class MultimeterTest(BaseMultimeter, VisaCompTest):
    """Виртуальный мультиметр для отладки без железа.

    Отвечает на любой запрос timestamp (порт 'test'), команды записи
    логируются. Все измерения доступны как у реального прибора.
    """

    _comm_list = multimeter_test_commands

    def __init__(self, port: str = TEST_PORT):
        super().__init__(port)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)

    with MultimeterTest() as multik:
        print('IDN ->', multik.identify_yourself())
        print('Vdc =', multik.meas.voltage_dc)
        print('R   =', multik.meas.resistance)
