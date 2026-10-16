from .base_sourse_meter import CommList, DeviceSpecs, BaseSourceMeter
from ..base_classes.visa_comp_test import VisaCompTest, TEST_PORT

sourse_meter_test_commands = CommList(
    set_voltage=":SOURce:VOLTage {voltage_V}",
    ask_voltage=":SOURce:VOLTage?",
    set_current_limit=":SOURce:VOLTage:ILIMit {curr_lim_A}",
    ask_current_limit=":SOURce:VOLTage:ILIMit?",

    meas_current=":MEASure:CURRent?",
    meas_voltage=":MEASure:VOLTage?",

    ask_state=":OUTPut?",
    set_on=":OUTPut ON",
    set_off=":OUTPut OFF",

    # compliance query: 1 = current limit tripped (CC), 0 = normal (CV)
    ask_mode=":SOURce:VOLTage:ILIMit:TRIPped?",
    answer_CC='1',
    answer_CV='0',
)

sourse_meter_test_specs = DeviceSpecs(
    max_time_wait=2.0,
    delay=0.1,
    tolerance=0.02,
)


class SourceMeterTest(BaseSourceMeter, VisaCompTest):
    """Виртуальный сурсметр для отладки без железа.

    Отвечает на любой запрос timestamp (порт 'test'), команды записи
    логируются. Полный API (set/meas/on/off/safe_on) доступен
    как у реального прибора.
    """

    def __init__(self, port: str = TEST_PORT):
        super().__init__(port, sourse_meter_test_commands, sourse_meter_test_specs)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)

    with SourceMeterTest() as smu:
        print('IDN ->', smu.identify_yourself())
        smu.set.voltage = 1
        smu.set.current_limit = 0.1
        smu.on()
        print('V =', smu.meas.voltage, 'I =', smu.meas.current)
