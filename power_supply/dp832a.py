from .base_power_supply import CommList, DeviceSpecs, PowerSupply, Channel

dp832_commands = CommList(
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
    answer_CC = 'CC',
    answer_CV= 'CV',
    answer_UR= 'UR'
)

# 2. Создать DeviceSpecs
dp832_specs = DeviceSpecs(
    max_time_wait=2.0,
    delay=0.1,
    channel_tolerance=0.02
)

class DP832A(PowerSupply):
    def __init__(self, port: str = ''):
        super().__init__(port, dp832_commands, dp832_specs)



if __name__ == "__main__":
    ps = DP832A('USB0::0x1AB1::0x0E11::DP8B262201226::INSTR')
    with ps:
        ps.channel_1.set.voltage = 1
        ps.channel_1.safe_on()
