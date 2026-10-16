from ..base_classes import VisaComp
from dataclasses import dataclass


@dataclass
class CommList:
    set_state_on: str
    set_state_off: str

    set_current: str = ''
    set_resistance: str = ''

    ask_state: str = ''
    meas_voltage: str = ''
    meas_current: str = ''
    meas_power: str = ''


class BaseLoad(VisaComp):
    """Базовый класс электронной нагрузки (SCPI-совместимой, VISA).

    Конкретные нагрузки задают только CommList с командами.
    Поля CommList, не поддерживаемые прибором, оставляют пустыми —
    вызов соответствующего метода бросит AssertionError.
    """

    def __init__(self, port: str, comm_list: CommList):
        super().__init__(port)
        self._comm_list = comm_list

    # --- Состояние нагрузки ---

    def load_on(self):
        self._set_parameter(self._comm_list.set_state_on)
        return self

    def load_off(self):
        self._set_parameter(self._comm_list.set_state_off)
        return self

    @property
    def is_load_on(self) -> bool:
        assert self._comm_list.ask_state != '', "No function ask state"
        return bool(int(self._ask_parameter(self._comm_list.ask_state)))

    # --- Установка режима ---

    def set_curr(self, curr: float):
        """Задать ток нагрузки (режим CC)."""
        assert self._comm_list.set_current != '', "No function set current"
        self._set_parameter(self._comm_list.set_current.format(curr=curr))
        return self

    def set_res(self, load_resistance_ohm: float):
        """Задать сопротивление нагрузки (режим CR)."""
        assert self._comm_list.set_resistance != '', "No function set resistance"
        self._set_parameter(
            self._comm_list.set_resistance.format(res=load_resistance_ohm)
        )
        return self

    # --- Измерения ---

    def read_volt(self) -> float:
        assert self._comm_list.meas_voltage != '', "No function meas voltage"
        return float(self._ask_parameter(self._comm_list.meas_voltage))

    def read_curr(self) -> float:
        assert self._comm_list.meas_current != '', "No function meas current"
        return float(self._ask_parameter(self._comm_list.meas_current))

    def read_pow(self) -> float:
        assert self._comm_list.meas_power != '', "No function meas power"
        return float(self._ask_parameter(self._comm_list.meas_power))
