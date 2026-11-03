from .base_sourse_meter import CommList, DeviceSpecs, BaseSourceMeter
from ..base_classes.visa_comp_test import VisaCompTest, TEST_PORT

sourse_meter_test_commands = CommList(
    set_mode_cv=":SOURce{channel}:FUNCtion:MODE VOLT",
    set_mode_cc=":SOURce{channel}:FUNCtion:MODE CURR",
    ask_mode=":SOURce{channel}:FUNCtion:MODE?",
    answer_CV='VOLT',
    answer_CC='CURR',

    set_voltage=":SOURce{channel}:VOLTage {voltage_V}",
    ask_voltage=":SOURce{channel}:VOLTage?",
    set_current=":SOURce{channel}:CURRent {curr_A}",
    ask_current=":SOURce{channel}:CURRent?",

    set_i_limit=":SOURce{channel}:VOLTage:ILIMit {curr_lim_A}",
    ask_i_limit=":SOURce{channel}:VOLTage:ILIMit?",
    set_v_limit=":SOURce{channel}:CURRent:VLIMit {volt_lim_V}",
    ask_v_limit=":SOURce{channel}:CURRent:VLIMit?",

    meas_current=":MEASure{channel}:CURRent?",
    meas_voltage=":MEASure{channel}:VOLTage?",
    meas_resistance=":MEASure{channel}:RESistance?",

    ask_state=":OUTPut{channel}?",
    set_on=":OUTPut{channel} ON",
    set_off=":OUTPut{channel} OFF",
)

sourse_meter_test_specs = DeviceSpecs(
    max_time_wait=2.0,
    delay=0.1,
    tolerance=0.02,
    num_channels=2,
)


class SourceMeterTest(BaseSourceMeter, VisaCompTest):
    """Виртуальный сурсметр (2 канала) для отладки без железа.

    Отвечает на любой запрос timestamp (порт 'test'), команды записи
    логируются. Полный API каналов (mode/set/limit/meas/on/off) доступен
    как у реального прибора.
    """

    def __init__(self, port: str = TEST_PORT):
        super().__init__(port, sourse_meter_test_commands, sourse_meter_test_specs)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)

    with SourceMeterTest() as smu:
        print('IDN ->', smu.identify_yourself())
        ch = smu.channel_1
        ch.mode.cv()
        ch.set.voltage = 1
        ch.limit.current = 0.1
        ch.on()
        print('CH1: V =', ch.meas.voltage, 'I =', ch.meas.current)

        ch2 = smu.channel_2
        ch2.mode.cc()
        ch2.set.current = 1e-3
        ch2.limit.voltage = 5
        ch2.on()
        print('CH2: I =', ch2.meas.current, 'V =', ch2.meas.voltage)

        smu.all_channels_off()
