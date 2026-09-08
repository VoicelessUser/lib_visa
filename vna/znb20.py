from dataclasses import dataclass
from ..base_classes import VisaComp
from math import floor, ceil




@dataclass
class ZNB20Commands:
    """Контейнер для SCPI команд анализатора цепей ZNB20"""
    
    # Sweep type commands
    SWEEP_TYPE_LIN: str = ":SWEep:TYPE LIN;"
    SWEEP_TYPE_LOG: str = ":SWEep:TYPE LOG;"
    SWEEP_TYPE_POW: str = ":SWEep:TYPE POW;"
    SWEEP_TYPE_CW: str = ":SWEep:TYPE CW;"
    
    # Power sweep commands
    POWER_START: str = ":SOURce{chanel}:POWer:STARt {power_dbm};"
    POWER_STOP: str = ":SOURce{chanel}:POWer:STOP {power_dbm};"
    SOURCE_FREQUENCY: str = ":SOURce{chanel}:FREQuency {freq_hz};"
    SOURCE_POWER: str = ":SOURce{chanel}:POWer {power};"
    
    # Frequency commands
    CW_FREQUENCY: str = ":FREQuency:CW {freq_hz};"
    FREQ_START: str = ":SENS:FREQ:STAR {freq_start};"
    FREQ_STOP: str = ":SENS:FREQ:STOP {freq_stop};"
    
    # Sweep settings
    SWEEP_POINTS: str = ":SWEep:POINts {points};"
    SWEEP_TIME: str = ":SWEep:TIME {time_sec};"
    
    # Data queries
    TRACE_DATA: str = "CALC{channel}:DATA? FDAT"
    FREQ_DATA: str = "CALCulate{channel}:DATA:STIMulus?"
    SWEEP_POINTS_QUERY: str = ":SENS{channel}:SWE:POIN?"
    
    # Trace selection
    ACTIVE_TRACE: str = "CALC:PAR:SEL '{trace_name}';"


class SweepType:
    """Управление типом развертки"""
    
    def __init__(self, device: VisaComp, comlist: ZNB20Commands):
        self._device = device
        self._comlist = comlist

    def lin(self):
        """Установить линейный тип развертки (LIN)"""
        self._device._set_parameter(self._comlist.SWEEP_TYPE_LIN)
        return self._device

    def log(self):
        """Установить логарифмический тип развертки (LOG)"""
        self._device._set_parameter(self._comlist.SWEEP_TYPE_LOG)
        return self._device

    def pow(self):
        """Установить развертку по мощности (POW)"""
        self._device._set_parameter(self._comlist.SWEEP_TYPE_POW)
        return self._device

    def cw(self):
        """Установить режим непрерывной волны (CW)"""
        self._device._set_parameter(self._comlist.SWEEP_TYPE_CW)
        return self._device


class Frequency:
    """Управление частотой"""
    
    def __init__(self, device: VisaComp, comlist: ZNB20Commands):
        self._device = device
        self._comlist = comlist

    def set_range(self, freq_start: float, freq_stop: float):
        """Установить диапазон частот"""
        self._device._set_parameter(self._comlist.FREQ_START.format(freq_start=freq_start))
        self._device._set_parameter(self._comlist.FREQ_STOP.format(freq_stop=freq_stop))

    def set_cw(self, freq_hz: float):
        """Установить CW частоту в Гц"""
        self._device._set_parameter(self._comlist.CW_FREQUENCY.format(freq_hz=freq_hz))
    
    def set_source_frequency(self, chanel: int, freq_hz: float):
        """Установить POW частоту в Гц"""
        self._device._set_parameter(self._comlist.SOURCE_FREQUENCY.format(chanel=chanel, freq_hz=freq_hz))


class Power:
    """Управление мощностью"""
    
    def __init__(self, device: VisaComp, comlist: ZNB20Commands):
        self._device = device
        self._comlist = comlist

    def set_start(self,chanel:int, power_dbm: float):
        """Установить начальную мощность в dBm"""
        self._device._set_parameter(self._comlist.POWER_START.format(chanel=chanel, power_dbm=power_dbm))
    
    def set_stop(self,chanel:int, power_dbm: float):
        """Установить начальную мощность в dBm"""
        self._device._set_parameter(self._comlist.POWER_STOP.format(chanel=chanel, power_dbm=power_dbm))
    
    def set_range(self,chanel:int, power_start:float, power_stop:float):
        self.set_start(chanel=chanel, power_dbm= power_start)
        self.set_stop(chanel=chanel, power_dbm= power_stop)

    def set_source_power(self, chanel: int, power: float):
        """Установить FREQ мощность в дБм"""
        self._device._set_parameter(self._comlist.SOURCE_POWER.format(chanel=chanel, power=power))


class Sweep:
    """Управление разверткой"""
    
    def __init__(self, device: VisaComp, comlist: ZNB20Commands):
        self._device = device
        self._comlist = comlist

    def set_points(self, points: int):
        """Установить количество точек развертки"""
        self._device._set_parameter(self._comlist.SWEEP_POINTS.format(points=points))

    def set_time(self, time_sec: float):
        """Установить время развертки в секундах"""
        self._device._set_parameter(self._comlist.SWEEP_TIME.format(time_sec=time_sec))


class Meas:
    """Управление трассами и измерениями"""
    
    def __init__(self, device: VisaComp, comlist: ZNB20Commands):
        self._device = device
        self._comlist = comlist

    def set_active_trace(self, trace_name: str):
        """Установить активную трассу"""
        self._device._set_parameter(self._comlist.ACTIVE_TRACE.format(trace_name=trace_name))

    def amp_data(self, channel: int):
        """
        Возвращает данные указанной трассы
        :param channel: Номер канала (начиная с 1)
        :return: Данные трассы в формате списка чисел
        """
        response = self._device._ask_parameter(self._comlist.TRACE_DATA.format(channel=channel))
        if response.startswith("Error") or response == "Not connected":
            return []
        return [float(num) for num in response.split(',')]

    def freq_data(self, channel: int):
        """Возвращает данные частот для указанного канала"""
        response = self._device._ask_parameter(self._comlist.FREQ_DATA.format(channel=channel))
        if response.startswith("Error") or response == "Not connected":
            return []
        return [float(num) for num in response.split(',')]

    def points_quantity(self, channel: int) -> int:
        """
        Возвращает количество точек при свипировании
        :return: Количество точек (int)
        """
        response = self._device._ask_parameter(self._comlist.SWEEP_POINTS_QUERY.format(channel=channel))
        if response.startswith("Error") or response == "Not connected":
            return 0
        return int(response)
    
    def find_point(self, channel:int, point_freq_hz:float):
        freq_data = self.freq_data(channel)
        amp_data = self.amp_data(channel)
        if point_freq_hz >= max(freq_data) or point_freq_hz <min(freq_data):
            raise ValueError("Point frequency out of range")
        if self.points_quantity(channel) < 2:
            raise ValueError("Not enough points")
        step = freq_data[1] - freq_data[0]
        i_point = (point_freq_hz - freq_data[0]) / step
        point_amp_data = amp_data[floor(i_point)] + (amp_data[ceil(i_point)]  - amp_data[floor(i_point)])*(i_point - floor(i_point))
        return point_amp_data
    
    def find_list_points(self, channel: int, point_freqs_hz: list[float], freq_data: list[float]|None = None) -> list[float]:
        # Одно обращение к прибору

        amp_data = self.amp_data(channel)
        if freq_data is None:
            freq_data = self.freq_data(channel)

        
        if len(freq_data) < 2:
            raise ValueError("Not enough points")
        
        min_freq, max_freq = min(freq_data), max(freq_data)
        step = freq_data[1] - freq_data[0]
        
        results = []
        for point_freq_hz in point_freqs_hz:
            # Валидация для каждой точки
            if point_freq_hz >= max_freq or point_freq_hz < min_freq:
                raise ValueError(f"Point frequency {point_freq_hz} Hz out of range [{min_freq}, {max_freq})")
            
            # Линейная интерполяция
            i_point = (point_freq_hz - freq_data[0]) / step
            i_floor = floor(i_point)
            i_ceil = ceil(i_point)
            
            # Защита от выхода за границы массива
            if i_ceil >= len(amp_data):
                i_ceil = len(amp_data) - 1
            
            point_amp = amp_data[i_floor] + (amp_data[i_ceil] - amp_data[i_floor]) * (i_point - i_floor)
            results.append(point_amp)
        
        return results
    
    def find_ndb_point(self, x_data:list[float], y_data:list[float], n_db_value: float, x_skip:float = 0):
        """
        Находит частоту, на которой значение амплитуды равно начальному значению + n_db_value.
        
        :param x_data: Список частот (Гц)
        :param y_data: Список значений амплитуды (дБ)
        :param n_db_value: Искомое смещение в дБ относительно начального значения (например, -3)
        :param x_skip: Частота, до которой пропускать анализ (Гц)
        :return: Частота в Гц, где достигается искомое значение дБ
        """
        if len(x_data) < 2 or len(y_data) < 2:
            raise ValueError("Недостаточно точек для анализа")
        
        if len(x_data) != len(y_data):
            raise ValueError("Длины x_data и y_data должны совпадать")
        
        min_x, max_x = min(x_data), max(x_data)
        if x_skip >= max_x:
            raise ValueError("x_skip должен быть меньше максимальной частоты в данных")
        
        start_idx = 0
        for i, x in enumerate(x_data):
            if x >= x_skip:
                start_idx = i
                break
        
        trimmed_x = x_data[start_idx:]
        trimmed_y = y_data[start_idx:]
        
        start_y = trimmed_y[0]
        target_y = start_y + n_db_value
        
        if target_y > max(trimmed_y) or target_y < min(trimmed_y):
            return 99e9
        
        for i in range(len(trimmed_x) - 1):
            y1, y2 = trimmed_y[i], trimmed_y[i + 1]
            
            if y1 <= target_y:
                x1, x2 = trimmed_x[i], trimmed_x[i + 1]
                t = (target_y - y1) / (y2 - y1)
                result_x = x1 + t * (x2 - x1)
                
                return result_x
        
        raise ValueError(f"Значение {n_db_value} дБ не найдено в диапазоне")



class ZNB20(VisaComp):
    """
    Анализатор цепей Rohde & Schwarz ZNB20.
    Использует композицию для организации функциональности.
    """ 
    
    def __init__(self, port: str = ''):
        super().__init__(port)
        self._comlist = ZNB20Commands()
        
        # Композиция: подклассы функциональности
        self.sweep_type = SweepType(self, self._comlist)
        self.freq = Frequency(self, self._comlist)
        self.power = Power(self, self._comlist)
        self.sweep = Sweep(self, self._comlist)
        self.meas = Meas(self, self._comlist)
        



