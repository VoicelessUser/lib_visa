from .base_sourse_meter import CommList, DeviceSpecs, BaseSourceMeter

# B2962A: канал задаётся числовым префиксом (SOUR1:, SENS1:, OUTP1:),
# у MEAS — суффиксом списка каналов (@1). Префикс '1' допустим наравне
# с отсутствием префикса (SOUR: == SOUR1:).
# Команды сверены с Keysight_B2962A_Programming_Guide (Edition 6):
#   SOUR[c]:FUNC:MODE, SOUR[c]:VOLT:LEV:IMM:AMPL, SENS[c]:CURR:PROT, MEAS:VOLT? (@n)
b2962a_commands = CommList(
    set_mode_cv="SOUR{channel}:FUNC:MODE VOLT",
    set_mode_cc="SOUR{channel}:FUNC:MODE CURR",
    ask_mode="SOUR{channel}:FUNC:MODE?",
    answer_CV='VOLT',
    answer_CC='CURR',

    set_voltage="SOUR{channel}:VOLT:LEV:IMM:AMPL {voltage_V}",
    ask_voltage="SOUR{channel}:VOLT:LEV:IMM:AMPL?",
    set_current="SOUR{channel}:CURR:LEV:IMM:AMPL {curr_A}",
    ask_current="SOUR{channel}:CURR:LEV:IMM:AMPL?",

    # compliance задаётся в подсистеме SENSe (см. мануал, стр. 4-89)
    set_i_limit="SENS{channel}:CURR:PROT {curr_lim_A}",
    ask_i_limit="SENS{channel}:CURR:PROT?",
    set_v_limit="SENS{channel}:VOLT:PROT {volt_lim_V}",
    ask_v_limit="SENS{channel}:VOLT:PROT?",

    meas_voltage="MEAS:VOLT? (@{channel})",
    meas_current="MEAS:CURR? (@{channel})",

    ask_state="OUTP{channel}?",
    set_on="OUTP{channel} ON",
    set_off="OUTP{channel} OFF",
)

b2962a_specs = DeviceSpecs(
    max_time_wait=2.0,
    delay=0.1,
    tolerance=0.02,
    num_channels=2,
)


class B2962A(BaseSourceMeter):
    def __init__(self, port: str = ''):
        super().__init__(port, b2962a_commands, b2962a_specs)


if __name__ == "__main__":
    smu = B2962A('USB0::0x0957::0x9018::MY52350786::INSTR')
    with smu:
        # источник напряжения 5 В с защитой по току 10 мА
        ch = smu.channel_1
        ch.mode.cv()
        ch.set.voltage = 5
        ch.limit.current = 10e-3
        ch.safe_on()
        print(ch.meas.voltage, ch.meas.current)

        # источник тока 1 мА с защитой по напряжению 5 В
        ch2 = smu.channel_2
        ch2.mode.cc()
        ch2.set.current = 1e-3
        ch2.limit.voltage = 5
        ch2.safe_on()
        print(ch2.meas.current, ch2.meas.voltage)
