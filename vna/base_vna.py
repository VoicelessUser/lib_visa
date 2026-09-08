from ..base_classes import VisaComp
from dataclasses import dataclass

@dataclass
class CommList:
    sweep_type: str

class SweepType:
    def __init__(self, device: VisaComp, comm_list: CommList):
        self._device = device
        self._comm_list = comm_list

    def linear(self):
        self._device.set_parameter(self._comm_list.sweep_type_linear)

    def logarithmic(self):
        self._device.set_parameter(self._comm_list.sweep_type_logarithmic)

    def power(self):
        self._device.set_parameter(self._comm_list.sweep_type_power)

    def cw(self):
        self._device.set_parameter(self._comm_list.sweep_type_cw)


class Set:
    def __init__(self, device: VisaComp, comm_list: CommList):
        self._device = device
        self._comm_list = comm_list
        self.sweep_type = SweepType(device, comm_list)
        
    @property
    def start_frequency(self):
        return self._device.get_parameter(self._comm_list.ask_start_frequency)

    @start_frequency.setter
    def start_frequency(self, frequency_hz: float):
        self._device.set_parameter(self._comm_list.set_start_frequency.format(frequency_hz=frequency_hz))