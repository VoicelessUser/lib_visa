"""Тесты поиска пиков и гармоник MS2038C на реальных логах измерений.

Источник данных: ``test_data/HMC733LC4BTR_1.txt`` — лог прогона ГУН HMC733LC4B
(перестройка напряжением DP832A CH2, 0...23 В) на анализаторе спектра MS2038C
(SPAN 9...20 ГГц, 551 точка, RBW по умолчанию).

В логе 16 трасс:
- 0...9  — сигнал ГУНа в полосе (9.06, 10.12, 11.52, 12.94, 14.30, 15.60,
  16.86, 18.00, 19.04, 19.94 ГГц) и шумовая дорожка около -46 dBm;
- 10...15 — частота ГУНа ушла выше 20 ГГц, в полосе только шум.

Железо не нужно: записанные ответы прибора подставляются в `Trace`.
"""

import re
from pathlib import Path

import pytest

from .ms2038c import HARM_NO_DATA, MS2038CCommands, Trace

LOG_PATH = Path(__file__).resolve().parent / "test_data" / "HMC733LC4BTR_1.txt"

TRACE_RE = re.compile(r":TRACe:DATA\? 1; -> (.*)$")
START_RE = re.compile(r":SENSe:FREQuency:STARt\?; -> ([\d.]+)")
STOP_RE = re.compile(r":SENSe:FREQuency:STOP\?; -> ([\d.]+)")

START_HZ = 9e9
STOP_HZ = 20e9
POINTS = 551
STEP_HZ = (STOP_HZ - START_HZ) / (POINTS - 1)  # 20 МГц на точку

# Ожидаемые максимумы трасс: частота ГУНа растёт с напряжением перестройки,
# None — сигнала в полосе 9...20 ГГц нет (только шум).
EXPECTED_MAX_GHZ = [
    9.06, 10.12, 11.52, 12.94, 14.30, 15.60, 16.86, 18.00, 19.04, 19.94,
    None, None, None, None, None, None,
]
# Уровень максимума, dBm (для трасс с сигналом).
EXPECTED_MAX_DBM = [-0.87, 0.10, -1.38, -4.74, -1.96, -2.88, -5.68, -4.98, -6.82, -5.99]
# Пиков выше медианы на 10 дБ: у трассы 0 видна 2-я гармоника 18.12 ГГц.
EXPECTED_PEAK_COUNT = [2] + [1] * 9 + [0] * 6


class _FreqStub:
    """Заглушка `device.freq`: только start/stop."""

    def __init__(self, start: float, stop: float):
        self.start = start
        self.stop = stop


class _DeviceStub:
    """Минимальная заглушка VisaComp: на любой запрос отдаёт записанный ответ."""

    def __init__(self, response: str, start: float, stop: float):
        self.response = response
        self.freq = _FreqStub(start, stop)

    def _ask_parameter(self, command: str) -> str:
        return self.response


class _LoggedTrace(Trace):
    """Trace поверх ответа, записанного в лог: прибор не нужен."""

    def __init__(self, response: str, start: float = START_HZ, stop: float = STOP_HZ):
        super().__init__(_DeviceStub(response, start, stop), MS2038CCommands())


def _parse_log(path: Path) -> tuple[float, float, list[str]]:
    """Достаёт из лога границы развёртки и сырые ответы `:TRACe:DATA? 1`."""
    start, stop = START_HZ, STOP_HZ
    responses: list[str] = []
    for line in path.read_text(encoding='utf-8', errors='replace').splitlines():
        match = TRACE_RE.search(line)
        if match:
            responses.append(match.group(1).strip())
            continue
        match = START_RE.search(line)
        if match:
            start = float(match.group(1))
            continue
        match = STOP_RE.search(line)
        if match:
            stop = float(match.group(1))
    return start, stop, responses


@pytest.fixture(scope='module')
def logs() -> tuple[float, float, list[str]]:
    if not LOG_PATH.exists():
        pytest.skip(f'нет файла лога: {LOG_PATH}')
    return _parse_log(LOG_PATH)


@pytest.fixture(scope='module')
def traces(logs) -> list[_LoggedTrace]:
    start, stop, responses = logs
    return [_LoggedTrace(response, start, stop) for response in responses]


# --- Разбор ответа прибора -------------------------------------------------

def test_log_contains_all_traces(logs):
    start, stop, responses = logs
    assert (start, stop) == (START_HZ, STOP_HZ)
    assert len(responses) == len(EXPECTED_MAX_GHZ)


def test_block_header_length_matches_payload(logs):
    for response in logs[2]:
        assert response.startswith('#4')
        declared = int(response[2:6])  # #4<nnnn>
        assert len(Trace._strip_block_header(response)) == declared


def test_strip_block_header_edge_cases():
    assert Trace._strip_block_header('#0') == ''          # нет данных
    assert Trace._strip_block_header('#13abc') == 'abc'   # 1 цифра длины
    assert Trace._strip_block_header('1.0,2.0') == '1.0,2.0'  # без заголовка


def test_read_amp_gives_551_points(traces):
    for trace in traces:
        amplitudes = trace.read_amp()
        assert len(amplitudes) == POINTS
        assert all(isinstance(value, float) for value in amplitudes)


def test_read_trace_builds_frequency_axis(traces):
    points = traces[0].read_trace()
    assert len(points) == POINTS
    assert points[0][0] == pytest.approx(START_HZ)
    assert points[-1][0] == pytest.approx(STOP_HZ)
    assert points[1][0] - points[0][0] == pytest.approx(STEP_HZ)


# --- Поиск максимума и пиков ----------------------------------------------

def test_find_max_is_global_maximum(traces):
    """find_max обязан совпадать с прямым перебором по записанной трассе."""
    for trace in traces:
        amplitudes = trace.read_amp()
        best = max(range(len(amplitudes)), key=amplitudes.__getitem__)
        freq, amp = trace.find_max()
        assert amp == pytest.approx(amplitudes[best])
        assert freq == pytest.approx(START_HZ + best * STEP_HZ)


def test_find_max_matches_golden_values(traces):
    """Частоты совпадают с реальной перестройкой ГУНа (±1 точка развёртки)."""
    for index, trace in enumerate(traces):
        freq, amp = trace.find_max()
        expected = EXPECTED_MAX_GHZ[index]
        if expected is None:
            # сигнала в полосе нет — максимум это шумовая дорожка
            assert amp < -30.0
            continue
        assert freq == pytest.approx(expected * 1e9, abs=STEP_HZ)
        assert amp == pytest.approx(EXPECTED_MAX_DBM[index], abs=1.0)


def test_peak_count_above_noise(traces):
    """Порог «медиана + 10 дБ» не даёт ложных пиков в шумовой дорожке."""
    for index, trace in enumerate(traces):
        amplitudes = trace.read_amp()
        height = Trace._noise_level(amplitudes) + 10.0
        peaks = Trace._find_peaks(amplitudes, height)
        assert len(peaks) == EXPECTED_PEAK_COUNT[index], f'трасса {index}'


def test_noise_level_is_median(traces):
    amplitudes = traces[0].read_amp()
    assert Trace._noise_level(amplitudes) == pytest.approx(
        sorted(amplitudes)[len(amplitudes) // 2]
    )
    assert Trace._noise_level([1.0, 2.0, 3.0, 9.0]) == pytest.approx(2.5)  # чётное число
    assert Trace._noise_level([1.0, 2.0, 3.0]) == pytest.approx(2.0)       # нечётное


def test_find_peaks_unit_cases():
    """Края трассы не пики, у плато берётся середина."""
    assert Trace._find_peaks([], 0.0) == []
    assert Trace._find_peaks([1.0], 0.0) == []
    assert Trace._find_peaks([1.0, 2.0], 0.0) == []
    assert Trace._find_peaks([5.0, 1.0, 1.0, 1.0], 0.0) == []  # максимум на краю
    assert Trace._find_peaks([1.0, 1.0, 1.0, 5.0], 0.0) == []
    assert Trace._find_peaks([0.0, 5.0, 5.0, 5.0, 0.0], 4.9) == [2]  # середина плато
    assert Trace._find_peaks([0.0, 5.0, 5.0, 5.0, 0.0], 5.1) == []  # не выше порога


# --- Поиск гармоник --------------------------------------------------------

def test_fundamental_is_single_strong_peak(traces):
    """f1 — самый левый пик, и на этих трассах он же глобальный максимум."""
    for index in range(10):
        trace = traces[index]
        (f1, a1), _, _ = trace.find_3_harm()
        noise = Trace._noise_level(trace.read_amp())
        assert f1 == pytest.approx(trace.find_max()[0])
        assert a1 > noise + 20.0


def test_fundamental_tracks_tuning_voltage(traces):
    """Частота f1 монотонно растёт с напряжением перестройки (лог 0...19.94 ГГц)."""
    freqs = [trace.find_3_harm()[0][0] for trace in traces[:10]]
    assert freqs == sorted(freqs)
    assert len(set(freqs)) == len(freqs)


def test_second_harmonic_found_when_in_band(traces):
    """При 0 В 2-я гармоника 18.12 ГГц попадает в полосу прибора."""
    (f1, a1), (f2, a2), (f3, a3) = traces[0].find_3_harm()
    assert f1 == pytest.approx(9.06e9, abs=STEP_HZ)
    assert a2 != HARM_NO_DATA
    assert f2 == pytest.approx(2 * f1, abs=f1 / 2)  # окно 2*f1 ± f1/2
    assert a2 == pytest.approx(-12.26, abs=1.5)
    assert a2 < a1
    # 3-я гармоника 27.18 ГГц — за пределами 9...20 ГГц
    assert (f3, a3) == (pytest.approx(3 * f1), HARM_NO_DATA)


def test_harmonics_out_of_band_marked_no_data(traces):
    """Для трасс 1...9 и 2-я, и 3-я гармоники выше 20 ГГц."""
    for index in range(1, 10):
        (f1, _), (f2, a2), (f3, a3) = traces[index].find_3_harm()
        assert f2 == pytest.approx(2 * f1)
        assert a2 == HARM_NO_DATA
        assert f3 == pytest.approx(3 * f1)
        assert a3 == HARM_NO_DATA


def test_no_signal_in_band_returns_none(traces):
    """Трассы 10...15 (перестройка 20...23 В): пиков выше шумов нет."""
    for index in range(10, len(traces)):
        assert traces[index].find_3_harm() is None, f'трасса {index}'


def test_threshold_filters_everything(traces):
    """Порог 60 дБ выше медианы не оставляет пиков ни на одной трассе."""
    for trace in traces:
        assert trace.find_3_harm(threshold_db=60.0) is None
