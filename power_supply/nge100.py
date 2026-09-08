from .base_power_supply import CommList, DeviceSpecs, PowerSupply, Channel

# 1. Создать CommList для NGE100
nge100_commands = CommList(
    set_voltage=":INST:NSEL {channel}; VOLT {voltage_V}",
    ask_voltage=":INST:NSEL {channel}; VOLT?",
    set_current_limit=":INST:NSEL {channel}; CURR {curr_lim_A}",
    ask_current_limit=":INST:NSEL {channel}; CURR?",

    meas_current=":INST:NSEL {channel}; MEAS:CURR?",
    meas_voltage=":INST:NSEL {channel}; MEAS:VOLT?",

    ask_state=":INST:NSEL {channel}; OUTP?",
    set_on=":INST:NSEL {channel}; OUTP ON",
    set_off=":INST:NSEL {channel}; OUTP OFF",
    ask_mode='',
    answer_CC = '',
    answer_CV='',
    answer_UR= ''
)

# 2. Создать DeviceSpecs
nge100_specs = DeviceSpecs(
    max_time_wait=2.0,
    delay=0.1,
    channel_tolerance=0.02  # 2%
)
class NGE100(PowerSupply):
    def __init__(self, port: str = ''):
        super().__init__(port, nge100_commands, nge100_specs)


if __name__ == "__main__":
    ps = NGE100()
    ps.port = 'USB0::0x1AB1::0x0E11::DP8B262201226::INSTR'
    with ps:
        ps.channel_1.set.voltage = 1
        ps.channel_1.safe_on()