from ..base_classes import VisaComp
from time import sleep
from dataclasses import dataclass


@dataclass
class CommList:
    set_voltage: str
    ask_voltage: str
    set_current_limit: str
    ask_current_limit: str

    meas_current: str
    meas_voltage: str

    ask_state: str
    set_on: str
    set_off: str

    ask_mode: str
    answer_CC: str
    answer_CV: str
    answer_UR: str = None


@dataclass
class DeviceSpecs:
    max_time_wait: float
    delay: float
    tolerance: float


class Set:
    def __init__(self, device: VisaComp, comm_list: CommList):
        self._device = device
        self._comm_list = comm_list

    @property
    def voltage(self) -> float:
        return float(self._device._ask_parameter(self._comm_list.ask_voltage))

    @voltage.setter
    def voltage(self, voltage_V: float):
        self._device._set_parameter(self._comm_list.set_voltage.format(voltage_V=voltage_V))

    @property
    def current_limit(self) -> float:
        return float(self._device._ask_parameter(self._comm_list.ask_current_limit))

    @current_limit.setter
    def current_limit(self, curr_lim_A: float):
        self._device._set_parameter(self._comm_list.set_current_limit.format(curr_lim_A=curr_lim_A))


class Meas:
    def __init__(self, device: VisaComp, comm_list: CommList):
        self._device = device
        self._comm_list = comm_list

    @property
    def current(self) -> float:
        return float(self._device._ask_parameter(self._comm_list.meas_current))

    @property
    def voltage(self) -> float:
        return float(self._device._ask_parameter(self._comm_list.meas_voltage))


class SourceMeter(VisaComp):
    def __init__(self, port: str, comm_list: CommList, specs: DeviceSpecs):
        super().__init__(port)
        self._comm_list = comm_list
        self._specs = specs
        self._max_time_wait = specs.max_time_wait
        self._delay = specs.delay
        self._tolerance = specs.tolerance

        self.set = Set(self, comm_list)
        self.meas = Meas(self, comm_list)

    @property
    def state(self) -> bool:
        return bool(int(self._ask_parameter(self._comm_list.ask_state)))

    def on(self):
        self._set_parameter(self._comm_list.set_on)

    def off(self):
        self._set_parameter(self._comm_list.set_off)

    def wait_for_target_voltage(self, target_voltage: float):
        for _ in range(int(self._max_time_wait / self._delay)):
            mode = self._ask_parameter(self._comm_list.ask_mode).strip()

            if mode == self._comm_list.answer_CV or mode == self._comm_list.answer_UR:
                actual_voltage = self.meas.voltage
                if target_voltage != 0:
                    if abs(target_voltage - actual_voltage) / target_voltage < self._tolerance:
                        break
                else:
                    if actual_voltage < self._tolerance:
                        break

            elif mode == self._comm_list.answer_CC:
                self.off()
                self.logger.error('Сурсметр в compliance (CC) — коротит')
                raise RuntimeError('Сурсметр коротит (CC / compliance)')

            else:
                self.logger.error(f'Неизвестный режим: {mode}')
                raise ConnectionError(f'Сурсметр в режиме {mode}')

            sleep(self._delay)

    def safe_on(self):
        target_voltage = self.set.voltage

        # Этап 1: soft-start на 20%
        self.set.voltage = target_voltage / 5
        self.on()
        self.wait_for_target_voltage(target_voltage / 5)

        # Этап 2: полное напряжение
        self.set.voltage = target_voltage
        self.wait_for_target_voltage(target_voltage)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.off()
        self.disconnect()
