from .base_lcr import LCRCommands, BaseLcrMeter


class SetTypeCapacitance:
    """Класс для настройки измерений ёмкости (Capacitance)."""
    def __init__(self, device: BaseLcrMeter):
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
    def __init__(self, device: BaseLcrMeter):
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
    def __init__(self, device: BaseLcrMeter):
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
    def __init__(self, device: BaseLcrMeter):
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


class E4980(BaseLcrMeter):
    """LCR-метр Keysight E4980."""

    def __init__(self, port: str = ''):
        super().__init__(port=port)
        self.meas_type_capacitance = SetTypeCapacitance(self)
        self.meas_type_resistance = SetTypeResistance(self)
        self.monitor = Monitor(self)
        self.meas_type_inductance = SetTypeInductance(self)


if __name__ == '__main__':
    lcr = E4980('USB0::...::INSTR')
    with lcr:
        lcr.frequency = 1000
        lcr.meas_type_capacitance.parallel_measurement()
        print(lcr.meas)
