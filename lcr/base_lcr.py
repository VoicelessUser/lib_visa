from ..base_classes import VisaComp
from dataclasses import dataclass


@dataclass
class LCRCommands:
    # Команды для настройки частоты
    set_frequency: str = ':FREQuency:CW {frequency}'
    get_frequency: str = ':FREQuency:CW?'

    # Типы измерений импеданса (:FUNCtion:IMPedance:TYPE)
    set_type_capacitance_par: str = ':FUNCtion:IMPedance:TYPE CPD'  # Cp-D measurement
    set_type_esr: str = ':FUNCtion:IMPedance:TYPE CSRS'  # Cs-Rs measurement for ESR
    set_type_quality_factor: str = ':FUNCtion:IMPedance:TYPE CPQ'  # Cp-Q measurement
    set_type_cp_g: str = ':FUNC:IMP:TYPE CPG'  # Cp-G
    set_type_cp_rp: str = ':FUNC:IMP:TYPE CPRP'  # Cp-Rp
    set_type_cs_d: str = ':FUNC:IMP:TYPE CSD'  # Cs-D
    set_type_cs_q: str = ':FUNC:IMP:TYPE CSQ'  # Cs-Q

    # Команды для измерения индуктивности (Lp-серии)
    set_type_lp_d: str = ':FUNC:IMP:TYPE LPD'  # Lp-D
    set_type_lp_g: str = ':FUNC:IMP:TYPE LPG'  # Lp-G
    set_type_lp_q: str = ':FUNC:IMP:TYPE LPQ'  # Lp-Q
    set_type_lp_rdc: str = ':FUNC:IMP:TYPE LPRD'  # Lp-Rdc
    set_type_lp_rp: str = ':FUNC:IMP:TYPE LPRP'  # Lp-Rp

    # Команды для измерения индуктивности (Ls-серии)
    set_type_ls_d: str = ':FUNC:IMP:TYPE LSD'  # Ls-D
    set_type_ls_q: str = ':FUNC:IMP:TYPE LSQ'  # Ls-Q
    set_type_ls_rdc: str = ':FUNC:IMP:TYPE LSRD'  # Ls-Rdc
    set_type_ls_rs: str = ':FUNC:IMP:TYPE LSRS'  # Ls-Rs

    # Команды для измерения сопротивления и других параметров
    set_type_g_b: str = ':FUNC:IMP:TYPE GB'  # G-B
    set_type_r_x: str = ':FUNC:IMP:TYPE RX'  # R-X
    set_type_vdc_idc: str = ':FUNC:IMP:TYPE VDID'  # Vdc-Idc

    # Команды для измерения Y-параметров
    set_type_y_0d: str = ':FUNC:IMP:TYPE YTD'  # Y-0d
    set_type_y_0r: str = ':FUNC:IMP:TYPE YTR'  # Y-0r

    # Команды для измерения Z-параметров
    set_type_z_0d: str = ':FUNC:IMP:TYPE ZTD'  # Z-0d
    set_type_z_0r: str = ':FUNC:IMP:TYPE ZTR'  # Z-0r

    # Основные команды для получения измерений
    get_measurement: str = ':*TRG;\n:FETCh:IMPedance?'  # Основная команда для получения измерений
    get_complex_measurement: str = ':FETCh:IMPedance:CORRected'  # Сложные измерения
    get_formatted_measurement: str = ':FETCh:IMPedance:FORMatted'  # Форматированные измерения

    # Команды для мониторинга
    get_ac_current: str = ':FETCh:SMONitor:IAC'  # Мониторинг AC тока
    get_dc_current: str = ':FETCh:SMONitor:IDC'  # Мониторинг DC тока
    get_ac_voltage: str = ':FETCh:SMONitor:VAC'  # Мониторинг AC напряжения
    get_dc_voltage: str = ':FETCh:SMONitor:VDC'  # Мониторинг DC напряжения

    set_alc_state: str = ':AMPLitude:ALC {state}'
    get_alc_state: str = ':AMPLitude:ALC?'
    set_volt: str = ':VOLT:LEV {voltage}'
    get_volt: str = ':VOLT:LEV?'


class BaseLcrMeter(VisaComp):
    """Базовый класс LCR-метра (Agilent/Keysight-style SCPI).

    Определяет общие команды: частота, уровень напряжения, ALC,
    триггер + чтение измерения, мониторинг. Типы измерений
    (Cp-D, Ls-Rs и т.д.) задаются в конкретном приборе.
    """

    def __init__(self, port: str, commands: LCRCommands = LCRCommands()):
        super().__init__(port=port)
        self._commands = commands

    @property
    def frequency(self) -> float:
        return float(self._ask_parameter(self._commands.get_frequency))

    @frequency.setter
    def frequency(self, frequency: float):
        self._set_parameter(self._commands.set_frequency.format(frequency=frequency))

    @property
    def meas(self) -> list[float]:
        answer = self._ask_parameter(self._commands.get_measurement)
        return [float(i) for i in answer.split(',')]

    @property
    def main_meas(self) -> float:
        return self.meas[0]

    @property
    def side_meas(self) -> float:
        return self.meas[1]

    @property
    def alc_state(self) -> bool:
        """Состояние ALC (Auto Level Control)."""
        return bool(int(self._ask_parameter(self._commands.get_alc_state)))

    @alc_state.setter
    def alc_state(self, state: bool):
        self._set_parameter(self._commands.set_alc_state.format(state=1 if state else 0))

    @property
    def voltage(self) -> float:
        """Уровень тестового напряжения в вольтах."""
        return float(self._ask_parameter(self._commands.get_volt))

    @voltage.setter
    def voltage(self, volt: float):
        if volt <= 0:
            raise ValueError(f"Напряжение должно быть положительным, получено {volt}")
        self._set_parameter(self._commands.set_volt.format(voltage=volt))

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.disconnect()
