from .base_load import CommList, BaseLoad
from ..base_classes.visa_comp_test import VisaCompTest, TEST_PORT

load_test_commands = CommList(
    set_state_on=":SOUR:INP:STAT 1",
    set_state_off=":SOUR:INP:STAT 0",

    set_current=":SOUR:CURR {curr}",
    set_resistance=":SOUR:RES:LEV:IMM {res}",

    ask_state=":SOUR:INP:STAT?",

    meas_voltage=":MEASure:VOLTage?",
    meas_current=":MEASure:CURRent?",
    meas_power=":MEASure:POWer?",
)


class LoadTest(BaseLoad, VisaCompTest):
    """Виртуальная электронная нагрузка для отладки без железа.

    Отвечает на любой запрос timestamp (порт 'test'), команды записи
    логируются. Полный API нагрузки доступен как у реального прибора.
    """

    def __init__(self, port: str = TEST_PORT):
        super().__init__(port, load_test_commands)


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)

    with LoadTest() as load:
        print('IDN ->', load.identify_yourself())
        load.load_on().set_curr(0.5)
        print('V =', load.read_volt())
        print('I =', load.read_curr())
        load.load_off()
