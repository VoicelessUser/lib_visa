from .base_power_supply import CommList, DeviceSpecs, BasePowerSupply
from ..base_classes.visa_comp_test import VisaCompTest, TEST_PORT

power_supply_test_commands = CommList(
    set_voltage=":SOUR{channel}:VOLT {voltage_V}",
    ask_voltage=":SOUR{channel}:VOLT?",
    set_current_limit=":SOUR{channel}:CURR {curr_lim_A}",
    ask_current_limit=":SOUR{channel}:CURR?",

    meas_current=":MEAS:CURR? CH{channel}",
    meas_voltage=":MEAS:VOLT? CH{channel}",

    ask_state=":OUTP? CH{channel}",
    set_on=":OUTP CH{channel},ON",
    set_off=":OUTP CH{channel},OFF",

    ask_mode=':OUTPut:CVCC? CH{channel}',
    answer_CC='CC',
    answer_CV='CV',
    answer_UR='UR'
)

power_supply_test_specs = DeviceSpecs(
    max_time_wait=2.0,
    delay=0.1,
    channel_tolerance=0.02
)


class PowerSupplyTest(BasePowerSupply, VisaCompTest):
    """Виртуальный источник питания (3 канала) для отладки без железа.

    Отвечает на любой запрос timestamp (порт 'test'), команды записи
    логируются. Полный API каналов (set/meas/on/off/safe_on) доступен
    как у реального прибора.
    """

    def __init__(self, port: str = TEST_PORT):
        super().__init__(port, power_supply_test_commands, power_supply_test_specs)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)

    with PowerSupplyTest() as ps:
        print('IDN ->', ps.identify_yourself())
        ps.set_all_channels([1.0, 2.0, 3.3], [0.1, 0.1, 0.5])
        for ch in ps.channels:
            print(f'CH{ch.num_channel}: V={ch.meas.voltage}, I={ch.meas.current}')
        ps.all_channels_off()
