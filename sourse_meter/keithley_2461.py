from .base_sourse_meter import CommList, DeviceSpecs, BaseSourceMeter

# 2461 в SCPI-режиме (не TSP): синтаксис серии 2400.
# TODO: сверить set/ask_mode и set_v_limit с SCPI-справочником 2461
keithley2461_commands = CommList(
    set_mode_cv=":SOURce:FUNCtion:MODE VOLT",
    set_mode_cc=":SOURce:FUNCtion:MODE CURR",
    ask_mode=":SOURce:FUNCtion:MODE?",
    answer_CV='VOLT',
    answer_CC='CURR',

    set_voltage=":SOURce:VOLTage {voltage_V}",
    ask_voltage=":SOURce:VOLTage?",
    set_current=":SOURce:CURRent {curr_A}",
    ask_current=":SOURce:CURRent?",

    # compliance противоположной величины (Keithley: ILIMit/VLIMit)
    set_i_limit=":SOURce:VOLTage:ILIMit {curr_lim_A}",
    ask_i_limit=":SOURce:VOLTage:ILIMit?",
    set_v_limit=":SOURce:CURRent:VLIMit {volt_lim_V}",
    ask_v_limit=":SOURce:CURRent:VLIMit?",

    meas_current=":MEASure:CURRent?",
    meas_voltage=":MEASure:VOLTage?",
    meas_resistance=":MEASure:RESistance?",

    ask_state=":OUTPut?",
    set_on=":OUTPut ON",
    set_off=":OUTPut OFF",
)

keithley2461_specs = DeviceSpecs(
    max_time_wait=2.0,
    delay=0.1,
    tolerance=0.02,
    num_channels=1,
)


class Keithley2461(BaseSourceMeter):
    def __init__(self, port: str = ''):
        super().__init__(port, keithley2461_commands, keithley2461_specs)


if __name__ == "__main__":
    smu = Keithley2461('USB0::0x05E6::0x2461::04450529::INSTR')  # TODO: set real serial number
    with smu:
        ch = smu.channel_1
        ch.mode.cv()
        ch.set.voltage = 1
        ch.limit.current = 0.1
        ch.safe_on()
        print(ch.meas.voltage, ch.meas.current)
