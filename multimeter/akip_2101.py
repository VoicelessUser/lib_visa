from ..base_classes import VisaComp
from dataclasses import dataclass

@dataclass
class CommList:
    voltage_dc: str
    voltage_ac: str
    current_dc: str
    current_ac: str
    resistance: str
    frequency: str
    capacitance: str
    continuity: str
    diode: str
    temperature: str

class Meas:
    def __init__(self, multimeter: VisaComp, comm_list: CommList):
        self._multimeter = multimeter
        self._comm_list = comm_list
        # Словарь для сопоставления команды конфигурации с коротким именем функции
        self._func_map = {
            comm_list.voltage_dc: 'VOLT',
            comm_list.voltage_ac: 'VOLT:AC',
            comm_list.current_dc: 'CURR',
            comm_list.current_ac: 'CURR:AC',
            comm_list.resistance: 'RES',
            comm_list.frequency: 'FREQ',
            comm_list.capacitance: 'CAP',
            comm_list.continuity: 'CONT',
            comm_list.diode: 'DIOD',
            comm_list.temperature: 'TEMP'
        }

    def _get_measurement(self, config_cmd: str, func_name: str) -> float:
        """Универсальный метод измерения с проверкой режима."""
        assert config_cmd != '', f"No function {func_name}"
        
        # Спрашиваем текущий режим
        current_mode = self._multimeter._ask_parameter('CONF?')
        # Парсим ответ (убираем кавычки и берём первое слово)
        current_func = current_mode.strip('"').split(',')[0].split()[0]
        
        # Ожидаемая функция
        expected_func = self._func_map.get(config_cmd, '')
        
        # Если режим не совпадает — переключаем
        if current_func != expected_func:
            self._multimeter._set_parameter(config_cmd)
        
        # Делаем измерение
        return float(self._multimeter._ask_parameter('READ?'))

    @property
    def voltage_dc(self):
        return self._get_measurement(self._comm_list.voltage_dc, "voltage dc")

    @property
    def voltage_ac(self):
        return self._get_measurement(self._comm_list.voltage_ac, "voltage ac")

    @property
    def current_dc(self):
        return self._get_measurement(self._comm_list.current_dc, "current dc")

    @property
    def current_ac(self):
        return self._get_measurement(self._comm_list.current_ac, "current ac")

    @property
    def resistance(self):
        return self._get_measurement(self._comm_list.resistance, "resistance")

    @property
    def frequency(self):
        return self._get_measurement(self._comm_list.frequency, "frequency")

    @property
    def capacitance(self):
        return self._get_measurement(self._comm_list.capacitance, "capacitance")

    @property
    def continuity(self):
        return self._get_measurement(self._comm_list.continuity, "continuity")

    @property
    def diode(self):
        return self._get_measurement(self._comm_list.diode, "diode")

    @property
    def temperature(self):
        return self._get_measurement(self._comm_list.temperature, "temperature")


class AKIP2101(VisaComp):
    def __init__(self, port: str):
        super().__init__(port)
        self._comm_list: CommList = CommList(
            voltage_dc='CONF:VOLT:DC',
            voltage_ac='CONF:VOLT:AC',
            current_dc='CONF:CURR:DC',
            current_ac='CONF:CURR:AC',
            resistance='CONF:RES',
            frequency='CONF:FREQ',
            capacitance='CONF:CAP',
            continuity='CONF:CONT',
            diode='CONF:DIODE',
            temperature='CONF:TEMP'
        )
        self.meas: Meas = None  # Инициализируем в connect

    def connect(self):
        super().connect()
        self.meas = Meas(self, self._comm_list)
        # Не устанавливаем начальный режим, пусть будет как есть

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()