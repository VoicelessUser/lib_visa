"""АКИП-2101 — это OEM-версия Siglent SDM3045X.

Команды соответствуют SDM3045X Programming Manual
(manuals/SDM3045X_ProgrammingManual_EN.pdf):
  * CONFigure:<function> — выбирает функцию, диапазон и разрешение,
    но измерение НЕ запускает (Range сбрасывается в AUTO);
  * READ?                — запускает измерение и возвращает результат;
  * CONFigure?           — возвращает функцию/диапазон/разрешение строкой
    вида "VOLT +2.00000000E-01". Сокращённые имена функций:
    VOLT, VOLT:AC, CURR, CURR:AC, RES, FREQ, CAP, CONT, DIOD, TEMP.
"""

from .base_multimeter import BaseMultimeter, CommList, Measurement

# Режим измерения задаётся отдельной командой CONF:*, результат всегда
# читается командой READ?. Перед измерением проверяем текущий режим (CONF?)
# и переключаем только при несовпадении с mode_id.
CommList_AKIP2101 = CommList(
    ask_mode='CONF?',
    # Явные настройки триггера обязательны: без них прибор со временем
    # зависает на READ? (с ними — 30/30 измерений без сбоев).
    setup=('TRIG:SOUR IMM', 'TRIG:COUN 1', 'SAMP:COUN 1'),
    voltage_dc=Measurement(read='READ?', config='CONF:VOLT:DC', mode_id='VOLT'),
    voltage_ac=Measurement(read='READ?', config='CONF:VOLT:AC', mode_id='VOLT:AC'),
    current_dc=Measurement(read='READ?', config='CONF:CURR:DC', mode_id='CURR'),
    current_ac=Measurement(read='READ?', config='CONF:CURR:AC', mode_id='CURR:AC'),
    resistance=Measurement(read='READ?', config='CONF:RES', mode_id='RES'),
    frequency=Measurement(read='READ?', config='CONF:FREQ', mode_id='FREQ'),
    capacitance=Measurement(read='READ?', config='CONF:CAP', mode_id='CAP'),
    continuity=Measurement(read='READ?', config='CONF:CONT', mode_id='CONT'),
    diode=Measurement(read='READ?', config='CONF:DIOD', mode_id='DIOD'),
    temperature=Measurement(read='READ?', config='CONF:TEMP', mode_id='TEMP'),
)


class AKIP2101(BaseMultimeter):
    """АКИП-2101 (OEM Siglent SDM3045X)."""

    _comm_list = CommList_AKIP2101
    # CONFigure сбрасывает диапазон в AUTO, и измерение с автодиапазоном
    # может идти заметно дольше стандартных 2 с.
    _default_timeout = 10000


# То же устройство под «родным» именем Siglent.
SDM3045X = AKIP2101


if __name__ == '__main__':
    multik = AKIP2101('address')
    with multik:
        print(multik.meas.voltage_dc)