from dataclasses import dataclass
import numpy as np
from time import sleep
from scipy.signal import find_peaks
from ..base_classes import VisaComp

MAX_FREQ_HZ = 20e9  # верхний частотный предел MS2038C
HARM_NO_DATA = -99.0  # метка "гармоника не измерена" в find_3_harm

@dataclass
class MS2038CCommands:
    """SCPI команды для анализатора спектра MS2038C (Spectrum Analyzer mode)."""

    # --- Frequency ---
    FREQ_CENTER: str = ":SENSe:FREQuency:CENTer {freq};"
    FREQ_CENTER_QUERY: str = ":SENSe:FREQuency:CENTer?;"
    FREQ_SPAN: str = ":SENSe:FREQuency:SPAN {freq};"
    FREQ_SPAN_QUERY: str = ":SENSe:FREQuency:SPAN?;"
    FREQ_START: str = ":SENSe:FREQuency:STARt {freq};"
    FREQ_START_QUERY: str = ":SENSe:FREQuency:STARt?;"
    FREQ_STOP: str = ":SENSe:FREQuency:STOP {freq};"
    FREQ_STOP_QUERY: str = ":SENSe:FREQuency:STOP?;"
    FREQ_SPAN_FULL: str = ":SENSe:FREQuency:SPAN:FULL;"

    # --- Bandwidth ---
    RBW: str = ":SENSe:BANDwidth:RESolution {freq};"
    RBW_QUERY: str = ":SENSe:BANDwidth:RESolution?;"
    RBW_AUTO: str = ":SENSe:BANDwidth:RESolution:AUTO {state};"
    RBW_AUTO_QUERY: str = ":SENSe:BANDwidth:RESolution:AUTO?;"
    VBW: str = ":SENSe:BANDwidth:VIDeo {freq};"
    VBW_QUERY: str = ":SENSe:BANDwidth:VIDeo?;"
    VBW_AUTO: str = ":SENSe:BANDwidth:VIDeo:AUTO {state};"
    VBW_AUTO_QUERY: str = ":SENSe:BANDwidth:VIDeo:AUTO?;"

    # --- Power / Attenuation ---
    ATTEN: str = ":SENSe:POWer:RF:ATTenuation {atten};"
    ATTEN_QUERY: str = ":SENSe:POWer:RF:ATTenuation?;"
    ATTEN_AUTO: str = ":SENSe:POWer:RF:ATTenuation:AUTO {state};"
    ATTEN_AUTO_QUERY: str = ":SENSe:POWer:RF:ATTenuation:AUTO?;"

    # --- Display (Reference Level & Scale) ---
    REF_LEVEL: str = ":DISPlay:WINDow:TRACe:Y:SCALe:RLEVel {ampl};"
    SCALE_PER_DIV: str = ":DISPlay:WINDow:TRACe:Y:SCALe:PDIVision {ampl};"
    REF_LEVEL_OFFSET: str = ":DISPlay:WINDow:TRACe:Y:SCALe:RLEVel:OFFSet {ampl};"

    # --- Detector ---
    DETECTOR: str = ":SENSe:DETector:FUNCtion {det};"

    # --- Average / Trace Mode ---
    AVERAGE_COUNT: str = ":SENSe:AVERage:COUNt {count};"
    AVERAGE_COUNT_QUERY: str = ":SENSe:AVERage:COUNt?;"
    AVERAGE_TYPE: str = ":SENSe:AVERage:TYPE {atype};"

    # --- Sweep ---
    SWEEP_TIME: str = ":SENSe:SWEep:TIME {time_sec};"
    SWEEP_TIME_QUERY: str = ":SENSe:SWEep:TIME?;"
    SWEEP_TIME_AUTO: str = ":SENSe:SWEep:TIME:AUTO {state};"
    SWEEP_TIME_AUTO_QUERY: str = ":SENSe:SWEep:TIME:AUTO?;"
    SWEEP_STATUS_QUERY: str = ":SENSe:SWEep:STATus?;"

    # --- Trigger / Initiate ---
    INIT_CONT: str = ":INITiate:CONTinuous {state};"
    INIT_CONT_QUERY: str = ":INITiate:CONTinuous?;"
    INIT_IMMEDIATE: str = ":INITiate:IMMediate;"

    # --- Trace ---
    TRACE_DATA: str = ":TRACe:DATA? {trace_num};"
    TRACE_PREAMBLE: str = ":TRACe:PREamble? {trace_num};"

    # --- Marker ---
    MARKER_X: str = ":CALCulate:MARKer{num}:X {freq};"
    MARKER_Y: str = ":CALCulate:MARKer{num}:Y?"
    MARKER_STATE: str = ":CALCulate:MARKer{num}:STATe {state};"
    MARKER_ALL_OFF: str = ":CALCulate:MARKer:AOFF;"

    # --- Common ---
    RESET: str = "*RST;"
    CLEAR_STATUS: str = "*CLS;"
    IDN: str = "*IDN?"


class Frequency:
    """Управление частотой спектрум-анализатора."""

    def __init__(self, device: VisaComp, comlist: MS2038CCommands):
        self._device = device
        self._comlist = comlist

    @property
    def center(self) -> float:
        """Центральная частота, Гц."""
        return float(self._device._ask_parameter(self._comlist.FREQ_CENTER_QUERY))

    @center.setter
    def center(self, freq: float):
        self._device._set_parameter(self._comlist.FREQ_CENTER.format(freq=freq))

    @property
    def span(self) -> float:
        """Полоса обзора, Гц."""
        return float(self._device._ask_parameter(self._comlist.FREQ_SPAN_QUERY))

    @span.setter
    def span(self, freq: float):
        self._device._set_parameter(self._comlist.FREQ_SPAN.format(freq=freq))

    @property
    def start(self) -> float:
        """Начальная частота, Гц."""
        return float(self._device._ask_parameter(self._comlist.FREQ_START_QUERY))

    @start.setter
    def start(self, freq: float):
        self._device._set_parameter(self._comlist.FREQ_START.format(freq=freq))

    @property
    def stop(self) -> float:
        """Конечная частота, Гц."""
        return float(self._device._ask_parameter(self._comlist.FREQ_STOP_QUERY))

    @stop.setter
    def stop(self, freq: float):
        self._device._set_parameter(self._comlist.FREQ_STOP.format(freq=freq))

    def full_span(self):
        """Полная полоса обзора (действие, не значение — поэтому метод)."""
        self._device._set_parameter(self._comlist.FREQ_SPAN_FULL)
        return self._device._ask_parameter(self._comlist.SWEEP_STATUS_QUERY)

    def set_start_stop(self, start: float, stop: float):
        """Установить диапазон start..stop, Гц."""
        self.start = start
        self.stop = stop
        return self._device._ask_parameter(self._comlist.SWEEP_STATUS_QUERY)

    def set_center_span(self, center: float, span: float):
        """Установить центр и полосу, Гц."""
        self.center = center
        self.span = span
        return self._device._ask_parameter(self._comlist.SWEEP_STATUS_QUERY)


class Bandwidth:
    """Управление полосами пропускания (RBW / VBW)."""

    def __init__(self, device: VisaComp, comlist: MS2038CCommands):
        self._device = device
        self._comlist = comlist

    @property
    def rbw(self) -> float:
        """Полоса разрешения, Гц."""
        return float(self._device._ask_parameter(self._comlist.RBW_QUERY))

    @rbw.setter
    def rbw(self, freq: float):
        self._device._set_parameter(self._comlist.RBW.format(freq=freq))

    @property
    def rbw_auto(self) -> bool:
        """Автовыбор RBW."""
        return self._device._ask_parameter(self._comlist.RBW_AUTO_QUERY).strip() in ('1', 'ON')

    @rbw_auto.setter
    def rbw_auto(self, state: bool):
        self._device._set_parameter(self._comlist.RBW_AUTO.format(state='ON' if state else 'OFF'))

    @property
    def vbw(self) -> float:
        """Видеополоса, Гц."""
        return float(self._device._ask_parameter(self._comlist.VBW_QUERY))

    @vbw.setter
    def vbw(self, freq: float):
        self._device._set_parameter(self._comlist.VBW.format(freq=freq))

    @property
    def vbw_auto(self) -> bool:
        """Автовыбор VBW."""
        return self._device._ask_parameter(self._comlist.VBW_AUTO_QUERY).strip() in ('1', 'ON')

    @vbw_auto.setter
    def vbw_auto(self, state: bool):
        self._device._set_parameter(self._comlist.VBW_AUTO.format(state='ON' if state else 'OFF'))


class PowerAtten:
    """Управление аттенюатором входа."""

    def __init__(self, device: VisaComp, comlist: MS2038CCommands):
        self._device = device
        self._comlist = comlist

    @property
    def attenuation(self) -> float:
        """Входное затухание, дБ."""
        return float(self._device._ask_parameter(self._comlist.ATTEN_QUERY))

    @attenuation.setter
    def attenuation(self, atten_db: float):
        self._device._set_parameter(self._comlist.ATTEN.format(atten=atten_db))

    @property
    def attenuation_auto(self) -> bool:
        """Автовыбор затухания."""
        return self._device._ask_parameter(self._comlist.ATTEN_AUTO_QUERY).strip() in ('1', 'ON')

    @attenuation_auto.setter
    def attenuation_auto(self, state: bool):
        self._device._set_parameter(self._comlist.ATTEN_AUTO.format(state='ON' if state else 'OFF'))


class Detector:
    """Тип детектора."""

    def __init__(self, device: VisaComp, comlist: MS2038CCommands):
        self._device = device
        self._comlist = comlist

    def set_detector(self, det: str):
        """
        POSitive | RMS | NEGative | SAMPle | QUASI
        """
        self._device._set_parameter(self._comlist.DETECTOR.format(det=det))
        return self._device


class Average:
    """Усреднение / режим трассы."""

    def __init__(self, device: VisaComp, comlist: MS2038CCommands):
        self._device = device
        self._comlist = comlist

    @property
    def count(self) -> int:
        """Число усреднений."""
        return int(float(self._device._ask_parameter(self._comlist.AVERAGE_COUNT_QUERY)))

    @count.setter
    def count(self, count: int):
        self._device._set_parameter(self._comlist.AVERAGE_COUNT.format(count=count))

    def set_type(self, atype: str):
        """
        NONE | SCALar | MAXimum | MINimum
        """
        self._device._set_parameter(self._comlist.AVERAGE_TYPE.format(atype=atype))
        return self._device


class Sweep:
    """Управление развёрткой."""

    def __init__(self, device: VisaComp, comlist: MS2038CCommands):
        self._device = device
        self._comlist = comlist

    @property
    def time(self) -> float:
        """Время развёртки, с."""
        return float(self._device._ask_parameter(self._comlist.SWEEP_TIME_QUERY))

    @time.setter
    def time(self, time_sec: float):
        self._device._set_parameter(self._comlist.SWEEP_TIME.format(time_sec=time_sec))

    @property
    def time_auto(self) -> bool:
        """Автовыбор времени развёртки."""
        return self._device._ask_parameter(self._comlist.SWEEP_TIME_AUTO_QUERY).strip() in ('1', 'ON')

    @time_auto.setter
    def time_auto(self, state: bool):
        self._device._set_parameter(self._comlist.SWEEP_TIME_AUTO.format(state='ON' if state else 'OFF'))


class Trigger:
    """Запуск измерения."""

    def __init__(self, device: VisaComp, comlist: MS2038CCommands):
        self._device = device
        self._comlist = comlist

    @property
    def continuous(self) -> bool:
        """Непрерывный запуск (ON/OFF)."""
        return self._device._ask_parameter(self._comlist.INIT_CONT_QUERY).strip() in ('1', 'ON')

    @continuous.setter
    def continuous(self, state: bool):
        self._device._set_parameter(self._comlist.INIT_CONT.format(state='ON' if state else 'OFF'))

    def single(self):
        self._device._set_parameter(self._comlist.INIT_IMMEDIATE)
        for _ in range(10):
            sleep(0.25)
            if self._device._ask_parameter(self._comlist.SWEEP_STATUS_QUERY) == '1':
                break


class Trace:
    """Работа с трассами."""

    def __init__(self, device: VisaComp, comlist: MS2038CCommands):
        self._device = device
        self._comlist = comlist

    @staticmethod
    def _strip_block_header(response: str) -> str:
        """Remove the IEEE-488.2 definite-block header (#AX) from a response."""
        if not response.startswith('#'):
            return response.strip()
        if response.startswith('#0'):  # invalid trace data
            return ''
        n_digits = int(response[1])
        n_bytes = int(response[2:2 + n_digits])
        return response[2 + n_digits: 2 + n_digits + n_bytes]

    def read_amp(self, trace_num: int = 1) -> list[float]:
        """Читает амплитуды трассы (текущие единицы, обычно dBm). Ошибка/невалид -> []."""
        response = self._device._ask_parameter(self._comlist.TRACE_DATA.format(trace_num=trace_num))
        if response.startswith("Error") or response == "Not connected":
            return []
        payload = self._strip_block_header(response)
        if not payload:
            return []
        return [float(point) for point in payload.split(',') if point.strip()]

    def read_preamble(self, trace_num: int = 1) -> dict[str, str] | None:
        """Читает заголовок трассы как словарь {NAME: VALUE}. Ошибка -> None."""
        response = self._device._ask_parameter(self._comlist.TRACE_PREAMBLE.format(trace_num=trace_num))
        if response.startswith("Error") or response == "Not connected":
            return None
        payload = self._strip_block_header(response)
        preamble: dict[str, str] = {}
        for pair in payload.split(','):
            name, sep, value = pair.partition('=')
            if sep:
                preamble[name.strip()] = value.strip()
        return preamble

    def read_trace(self, trace_num: int = 1) -> list[tuple[float, float]]:
        """Читает трассу целиком.

        Возвращает список кортежей (frequency, amplitude):
        - frequency — частота точки, Гц (ось X, от freq.start до freq.stop);
        - amplitude — уровень в текущих единицах прибора, обычно dBm (ось Y).

        Ось X строится по запросам freq.start / freq.stop (в SPA-режиме
        команды для чтения списка частот нет). Ошибка связи -> [].
        """
        amplitudes = self.read_amp(trace_num)
        if not amplitudes:
            return []
        try:
            start = self._device.freq.start
            stop = self._device.freq.stop
        except ValueError:  # нет связи: query вернул не число
            return []
        n = len(amplitudes)
        step = (stop - start) / (n - 1) if n > 1 else 0.0
        return [(start + i * step, amp) for i, amp in enumerate(amplitudes)]



    def find_max(self, trace_num: int = 1) -> tuple[float, float] | None:
        """Точка максимальной амплитуды трассы.

        Возвращает кортеж (frequency, amplitude):
        - frequency — частота максимума, Гц;
        - amplitude — уровень максимума (обычно dBm).

        Пустая трасса / ошибка -> None.
        """
        trace = self.read_trace(trace_num)
        if not trace:
            return None
        return max(trace, key=lambda point: point[1])

    

    @staticmethod
    def _noise_level(amps: np.ndarray) -> float:
        """Оценка уровня шумовой дорожки: медиана амплитуд (устойчива к пикам сигнала)."""
        return float(np.median(amps))

    def find_3_harm(self, trace_num: int = 1, threshold_db: float = 10.0) -> tuple[tuple[float, float], tuple[float, float], tuple[float, float]] | None:
        """Возвращает ((f1,a1),(f2,a2),(f3,a3)): f1 — самый левый локальный максимум, превышающий уровень шумов на threshold_db (по умолчанию 10 дБ), гармоники — наибольшие пики выше того же порога в окнах n*f1 ± f1/2. Если гармоника выше 20 ГГц, вне диапазона или не выше порога — amplitude = -99.0. Нет пиков выше порога / ошибка -> None."""
        trace = self.read_trace(trace_num)
        if not trace:
            return None
        data = np.asarray(trace, dtype=float)
        freqs, amps = data[:, 0], data[:, 1]

        noise = self._noise_level(amps)
        peak_idx, _ = find_peaks(amps, height=noise + threshold_db)  # пики выше шумов
        if peak_idx.size == 0:  # сигнала выше шумовой дорожки нет
            return None

        i1 = int(peak_idx[0])  # самый левый пик выше порога
        f1, a1 = float(freqs[i1]), float(amps[i1])

        def harmonic(mult: int) -> tuple[float, float]:
            freq_h = mult * f1
            if freq_h > MAX_FREQ_HZ or not freqs[0] <= freq_h <= freqs[-1]:
                return (freq_h, HARM_NO_DATA)
            window = (freqs >= freq_h - f1 / 2) & (freqs < freq_h + f1 / 2)
            cand = peak_idx[window[peak_idx]]
            if cand.size:  # наибольший пик выше порога в окне
                i = cand[int(np.argmax(amps[cand]))]
                return (float(freqs[i]), float(amps[i]))
            return (freq_h, HARM_NO_DATA)  # гармоника не выше шумов

        return ((f1, a1), harmonic(2), harmonic(3))


class Marker:
    """Управление маркерами."""

    def __init__(self, device: VisaComp, comlist: MS2038CCommands):
        self._device = device
        self._comlist = comlist

    def set_x(self, num: int, freq: float):
        self._device._set_parameter(self._comlist.MARKER_X.format(num=num, freq=freq))
        return self._device

    def read_y(self, num: int):
        response = self._device._ask_parameter(self._comlist.MARKER_Y.format(num=num))
        if response.startswith("Error") or response == "Not connected":
            return None
        return response

    def set_state(self, num: int, state: bool):
        self._device._set_parameter(self._comlist.MARKER_STATE.format(num=num, state='ON' if state else 'OFF'))
        return self._device

    def all_off(self):
        self._device._set_parameter(self._comlist.MARKER_ALL_OFF)
        return self._device


class MS2038C(VisaComp):
    """
    Анализатор спектра Anritsu MS2038C (Spectrum Analyzer mode).
    Использует композицию подклассов для организации функциональности.
    """

    def __init__(self, port: str = ''):
        super().__init__(port)
        self._timeout = 3000
        self._comlist = MS2038CCommands()

        # Композиция: подклассы функциональности
        self.freq = Frequency(self, self._comlist)
        self.bw = Bandwidth(self, self._comlist)
        self.power = PowerAtten(self, self._comlist)
        self.detector = Detector(self, self._comlist)
        self.average = Average(self, self._comlist)
        self.sweep = Sweep(self, self._comlist)
        self.trigger = Trigger(self, self._comlist)
        self.trace = Trace(self, self._comlist)
        self.marker = Marker(self, self._comlist)


