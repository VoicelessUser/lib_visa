from ..base_classes import VisaComp
from dataclasses import dataclass


@dataclass
class LCRCommands:
    # Команды для настройки частоты
    set_frequency: str = ':FREQuency:CW {frequency}'
    get_frequency: str = ':FREQuency:CW?'

    # Команды для измерения ёмкости
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




class SetTypeCapacitance:
    """Класс для настройки измерений ёмкости (Capacitance)."""
    def __init__(self, device: VisaComp):
        self.device = device

    def parallel_measurement(self):
        """Настраивает измерение ёмкости (параллельная модель Cp‑D)."""
        self.device._set_parameter(LCRCommands.set_type_capacitance_par)

    def esr_measurement(self):
        """Настраивает измерение ESR (Cs‑Rs)."""
        self.device._set_parameter(LCRCommands.set_type_esr)

    def quality_factor_measurement(self):
        """Настраивает измерение добротности (Cp‑Q)."""
        self.device._set_parameter(LCRCommands.set_type_quality_factor)

    def g_measurement(self):
        """Настраивает измерение ёмкости с коэффициентом потерь (Cp‑G)."""
        self.device._set_parameter(LCRCommands.set_type_cp_g)


    def rp_measurement(self):
        """Настраивает измерение ёмкости с сопротивлением (Cp‑Rp)."""
        self.device._set_parameter(LCRCommands.set_type_cp_rp)


    def series_d_measurement(self):
        """Настраивает измерение последовательной ёмкости (Cs‑D)."""
        self.device._set_parameter(LCRCommands.set_type_cs_d)


    def series_q_measurement(self):
        """Настраивает измерение последовательной ёмкости с добротностью (Cs‑Q)."""
        self.device._set_parameter(LCRCommands.set_type_cs_q)

class SetTypeInductance:
    """Класс для настройки измерений индуктивности (Inductance)."""
    def __init__(self, device: VisaComp):
        self.device = device

    def parallel_d_measurement(self):
        """Настраивает измерение индуктивности (параллельная модель, Lp‑D)."""
        self.device._set_parameter(LCRCommands.set_type_lp_d)

    def parallel_g_measurement(self):
        """Настраивает измерение индуктивности (параллельная модель, Lp‑G)."""
        self.device._set_parameter(LCRCommands.set_type_lp_g)


    def parallel_q_measurement(self):
        """Настраивает измерение индуктивности (параллельная модель, Lp‑Q)."""
        self.device._set_parameter(LCRCommands.set_type_lp_q)


    def parallel_rdc_measurement(self):
        """Настраивает измерение индуктивности (параллельная модель, Lp‑Rdc)."""
        self.device._set_parameter(LCRCommands.set_type_lp_rdc)

    def parallel_rp_measurement(self):
        """Настраивает измерение индуктивности (параллельная модель, Lp‑Rp)."""
        self.device._set_parameter(LCRCommands.set_type_lp_rp)


    def series_d_measurement(self):
        """Настраивает измерение индуктивности (последовательная модель, Ls‑D)."""
        self.device._set_parameter(LCRCommands.set_type_ls_d)


    def series_q_measurement(self):
        """Настраивает измерение индуктивности (последовательная модель, Ls‑Q)."""
        self.device._set_parameter(LCRCommands.set_type_ls_q)


    def series_rdc_measurement(self):
        """Настраивает измерение индуктивности (последовательная модель, Ls‑Rdc)."""
        self.device._set_parameter(LCRCommands.set_type_ls_rdc)

    def series_rs_measurement(self):
        """Настраивает измерение индуктивности (последовательная модель, Ls‑Rs)."""
        self.device._set_parameter(LCRCommands.set_type_ls_rs)

class SetTypeResistance:
    """Класс для настройки измерений сопротивления (Resistance) и других параметров."""
    def __init__(self, device: VisaComp):
        self.device = device

    def conductance_resistance_measurement(self):
        """Настраивает измерение проводимости и сопротивления (G‑B)."""
        self.device._set_parameter(LCRCommands.set_type_g_b)

    def resistance_reactance_measurement(self):
        """Настраивает измерение сопротивления и реактивного сопротивления (R‑X)."""
        self.device._set_parameter(LCRCommands.set_type_r_x)


    def voltage_current_dc_measurement(self):
        """Настраивает измерение постоянного напряжения и тока (Vdc‑Idc)."""
        self.device._set_parameter(LCRCommands.set_type_vdc_idc)

    def impedance_resistance_measurement(self):
        """Настраивает измерение импеданса и сопротивления (Z-R)."""
        self.device._set_parameter(LCRCommands.set_type_z_0r)

class Monitor:
    """Класс для мониторинга параметров."""
    def __init__(self, device: VisaComp):
        self.device = device

    def ac_current(self):
        """Мониторинг переменного тока (IAC)."""
        return self.device._ask_parameter(LCRCommands.get_ac_current)


    def dc_current(self):
        """Мониторинг постоянного тока (IDC)."""
        return self.device._ask_parameter(LCRCommands.get_dc_current)


    def ac_voltage(self):
        """Мониторинг переменного напряжения (VAC)."""
        return self.device._ask_parameter(LCRCommands.get_ac_voltage)

    def dc_voltage(self):
        """Мониторинг постоянного напряжения (VDC)."""
        return self.device._ask_parameter(LCRCommands.get_dc_voltage)


class E4980(VisaComp):
    def __init__(self, port: str = ''):
        super().__init__(port=port)
        self.meas_type_capacitance = SetTypeCapacitance(self)
        self.meas_type_resistance = SetTypeResistance(self)
        self.monitor = Monitor(self)
        self.meas_type_inductance = SetTypeInductance(self)


    @property
    def frequency(self)->float:
        return self._ask_parameter(LCRCommands.get_frequency)

    @frequency.setter
    def frequency(self, frequency: float):
        self._set_parameter(LCRCommands.set_frequency.format(frequency=frequency))

    @property
    def meas(self)->list[float]:
        answer = self._ask_parameter(LCRCommands.get_measurement)
        answer_list = [float(i) for i in answer.split(',')]
        return answer_list
    
    @property
    def alc_state(self) -> str:
        """Состояние ALC (Auto Level Control)."""
        return self._ask_parameter(LCRCommands.get_alc_state)

    @alc_state.setter
    def alc_state(self, state: bool):
        """
        Включить/выключить ALC.
        """
        self._set_parameter(LCRCommands.set_alc_state.format(state=1 if state else 0))

    @property
    def voltage(self) -> float:
        """Уровень тестового напряжения в вольтах."""
        return float(self._ask_parameter(LCRCommands.get_volt))

    @voltage.setter
    def voltage(self, volt: float):
        """
        Установить уровень тестового напряжения.
        Диапазон: обычно 5 мВ – 2 В для E4980, но валидацию лучше вынести в конфиг.
        """
        if volt <= 0:
            raise ValueError(f"Напряжение должно быть положительным, получено {volt}")
        self._set_parameter(LCRCommands.set_volt.format(voltage=volt))

    @property
    def main_meas(self) -> float:
       return self.meas[0]

    @property
    def side_meas(self) -> float:
       return self.meas[1]
    
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.disconnect()



