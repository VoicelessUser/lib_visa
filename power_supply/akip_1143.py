from .base_power_supply import CommList, DeviceSpecs, PowerSupply, Channel

akip_1143_commands = CommList(
    set_voltage="VOLT {voltage_V}",
    ask_voltage="VOLT?",
    set_current_limit="CURR {curr_lim_A}",
    ask_current_limit="CURR?",
    
    meas_current="MEAS:CURR?",
    meas_voltage="MEAS:VOLT?",
    
    ask_state="OUTP?",
    set_on="OUTP ON",
    set_off="OUTP OFF",
    ask_mode='',
    answer_CC = '',
    answer_CV='',
    answer_UR= 'UR'
)

# 2. Создать DeviceSpecs
akip_1143_specs = DeviceSpecs(
    num_channels=1,
    max_time_wait=2.0,
    delay=0.1,
    channel_tolerance=0.02
)

class AKIP1143(PowerSupply):
    def __init__(self, port: str = ''):
        super().__init__(port, akip_1143_commands, akip_1143_specs)


if __name__ == "__main__":
    ps = AKIP1143('USB0::0x2EC7::0x6700::805025013787010002::INSTR')
    with ps:
        ps.channel_1.set.voltage = 1
        ps.channel_1.safe_on()
