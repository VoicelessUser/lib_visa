from .base_sourse_meter import CommList, DeviceSpecs, SourceMeter

keithley2461_commands = CommList(
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

keithley2461_specs = DeviceSpecs(
    max_time_wait=2.0,
    delay=0.1,
    tolerance=0.02,
)


class Keithley2461(SourceMeter):
    def __init__(self, port: str = ''):
        super().__init__(port, keithley2461_commands, keithley2461_specs)


if __name__ == "__main__":
    smu = Keithley2461('USB0::0x05E6::0x2461::04450529::INSTR')  # TODO: set real serial number
    with smu:
        smu.set.voltage = 1
        smu.set.current_limit = 0.1
        smu.safe_on()
        print(smu.meas.voltage, smu.meas.current)
