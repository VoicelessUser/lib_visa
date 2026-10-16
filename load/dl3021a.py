from .base_load import CommList, BaseLoad

dl3021a_commands = CommList(
    set_state_on=":SOUR:INP:STAT 1",
    set_state_off=":SOUR:INP:STAT 0",

    set_current=":SOUR:CURR {curr}",
    set_resistance=":SOUR:RES:LEV:IMM {res}",

    meas_voltage=":MEASure:VOLTage?",
    meas_current=":MEASure:CURRent?",
    meas_power=":MEASure:POWer?",
)


class DL3021A(BaseLoad):
    def __init__(self, port: str = ''):
        super().__init__(port, dl3021a_commands)


if __name__ == '__main__':
    load = DL3021A('USB0::...::INSTR')
    with load:
        load.load_on().set_curr(0.5)
        print(load.read_volt())
        load.load_off()
