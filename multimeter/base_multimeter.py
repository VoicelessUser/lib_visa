from ..base_classes import VisaComp
from dataclasses import dataclass

@dataclass
class CommList:
    voltage_dc:str
    voltage_ac:str
    current_dc:str
    current_ac:str
    resistance:str
    frequency:str
    capacitance:str
    continuity:str
    diode:str
    temperature:str

class Meas:
    def __init__(self, multimeter:VisaComp, comm_list:CommList):
        self._multimeter = multimeter
        self._comm_list = comm_list

    @property
    def voltage_dc(self):
        assert self._comm_list.voltage_dc != '', "No function voltage dc"
        return float(self._multimeter._ask_parameter(self._comm_list.voltage_dc))

    @property
    def voltage_ac(self):
        assert self._comm_list.voltage_ac != '', "No function voltage ac"
        return float(self._multimeter._ask_parameter(self._comm_list.voltage_ac))

    @property
    def current_dc(self):
        assert self._comm_list.current_dc != '', "No function current dc"
        return float(self._multimeter._ask_parameter(self._comm_list.current_dc))

    @property
    def current_ac(self):
        assert self._comm_list.current_ac != '', "No function current ac"
        return float(self._multimeter._ask_parameter(self._comm_list.current_ac))

    @property
    def resistance(self):
        assert self._comm_list.resistance != '', "No function resistance"
        return float(self._multimeter._ask_parameter(self._comm_list.resistance))

    @property
    def frequency(self):
        assert self._comm_list.frequency != '', "No function frequency"
        return float(self._multimeter._ask_parameter(self._comm_list.frequency))

    @property
    def capacitance(self):
        assert self._comm_list.capacitance != '', "No function capacitance"
        return float(self._multimeter._ask_parameter(self._comm_list.capacitance))

    @property
    def continuity(self):
        assert self._comm_list.continuity != '', "No function continuity"
        return float(self._multimeter._ask_parameter(self._comm_list.continuity))

    @property
    def diode(self):
        assert self._comm_list.diode != '', "No function diode"
        return float(self._multimeter._ask_parameter(self._comm_list.diode))

    @property
    def temperature(self):
        assert self._comm_list.temperature != '', "No function temperature"
        return float(self._multimeter._ask_parameter(self._comm_list.temperature))

class Multimeter(VisaComp):
    def __init__(self, port:str):
        super().__init__(port)
        self._comm_list: CommList
        self.meas: Meas

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
