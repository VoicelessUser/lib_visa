from dataclasses import dataclass

from ..base_classes import VisaComp


@dataclass(frozen=True)
class Measurement:
    """Описание одного измерения прибора.

    read    — команда чтения результата (напр. ':MEAS:VOLT:DC?' или 'READ?').
    config  — команда переключения прибора в нужный режим (опционально).
    mode_id — ожидаемое имя функции в ответе на ask_mode (напр. 'VOLT').

    Приборы ведут себя по-разному:
      * DM3068 — режим задаёт сама команда read, поэтому config/mode_id пустые;
      * AKIP2101 — режим выставляем отдельной командой config, причём только
        если текущий режим прибора не совпадает с mode_id.
    """

    read: str = ''
    config: str = ''
    mode_id: str = ''


@dataclass
class CommList:
    """Набор команд мультиметра.

    ask_mode — команда запроса текущего режима (напр. 'CONF?').
               Пустая строка означает, что переключение режима не требуется.
    setup    — служебные команды (триггер/настройка), отправляемые перед
               каждым измерением. Каждый элемент — отдельное сообщение.
               Напр. AKIP2101: ('TRIG:SOUR IMM', 'TRIG:COUN 1', 'SAMP:COUN 1').
    """

    ask_mode: str = ''
    setup: tuple[str, ...] = ()
    voltage_dc: Measurement = Measurement()
    voltage_ac: Measurement = Measurement()
    current_dc: Measurement = Measurement()
    current_ac: Measurement = Measurement()
    resistance: Measurement = Measurement()
    frequency: Measurement = Measurement()
    capacitance: Measurement = Measurement()
    continuity: Measurement = Measurement()
    diode: Measurement = Measurement()
    temperature: Measurement = Measurement()


class Meas:
    """Единая логика измерений для всех мультиметров.

    Если у измерения заданы config и у прибора задан ask_mode — сначала
    спрашиваем текущий режим и переключаемся только при несовпадении.
    Иначе читаем напрямую, без лишних запросов (как у DM3068).
    """

    def __init__(self, multimeter: VisaComp, comm_list: CommList):
        self._multimeter = multimeter
        self._comm_list = comm_list

    def _ensure_mode(self, measurement: Measurement) -> None:
        """Переключает режим прибора, только если он отличается от нужного."""
        answer = self._multimeter._ask_parameter(self._comm_list.ask_mode)
        current = answer.strip('"').split(',')[0].split()[0]
        if current != measurement.mode_id:
            self._multimeter._set_parameter(measurement.config)

    def _read(self, measurement: Measurement, name: str) -> float:
        assert measurement.read != '', f"No function {name}"
        if measurement.config and self._comm_list.ask_mode:
            self._ensure_mode(measurement)
        for command in self._comm_list.setup:
            self._multimeter._set_parameter(command)
        return float(self._multimeter._ask_parameter(measurement.read))

    @property
    def voltage_dc(self) -> float:
        return self._read(self._comm_list.voltage_dc, "voltage dc")

    @property
    def voltage_ac(self) -> float:
        return self._read(self._comm_list.voltage_ac, "voltage ac")

    @property
    def current_dc(self) -> float:
        return self._read(self._comm_list.current_dc, "current dc")

    @property
    def current_ac(self) -> float:
        return self._read(self._comm_list.current_ac, "current ac")

    @property
    def resistance(self) -> float:
        return self._read(self._comm_list.resistance, "resistance")

    @property
    def frequency(self) -> float:
        return self._read(self._comm_list.frequency, "frequency")

    @property
    def capacitance(self) -> float:
        return self._read(self._comm_list.capacitance, "capacitance")

    @property
    def continuity(self) -> float:
        return self._read(self._comm_list.continuity, "continuity")

    @property
    def diode(self) -> float:
        return self._read(self._comm_list.diode, "diode")

    @property
    def temperature(self) -> float:
        return self._read(self._comm_list.temperature, "temperature")


class BaseMultimeter(VisaComp):
    """Базовый мультиметр.

    Наследник задаёт только _comm_list с командами конкретного прибора;
    вся логика (подключение, измерения, переключение режимов) — здесь.
    """

    _comm_list: CommList

    def __init__(self, port: str):
        super().__init__(port)
        self.meas = Meas(self, self._comm_list)
