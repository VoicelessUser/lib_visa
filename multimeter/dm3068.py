from .base_multimeter import Multimeter, Meas, CommList

CommList_DM3068 = CommList(
    voltage_dc = ':TRIG:COUN 1;:MEAS AUTO;:MEAS:VOLT:DC?',
    voltage_ac = ':TRIG:COUN 1;:MEAS AUTO;:MEAS:VOLT:AC?',
    current_dc = ':TRIG:COUN 1;:MEAS AUTO;:MEAS:CURR:DC?',
    current_ac = ':TRIG:COUN 1;:MEAS AUTO;:MEAS:CURR:AC?',
    resistance = ':TRIG:COUN 1;:MEAS AUTO;:MEAS:RES?',
    frequency = ':TRIG:COUN 1;:MEAS AUTO;:MEAS:FREQ?',
    capacitance = ':TRIG:COUN 1;:MEAS AUTO;:MEAS:CAP?',
    continuity = ':TRIG:COUN 1;:MEAS AUTO;:MEAS:CONT?',
    diode = ':TRIG:COUN 1;:MEAS AUTO;:MEAS:DIOD?',
    temperature = ''
)


class DM3068(Multimeter):
    def __init__(self, port: str):
        super().__init__(port)
        self._comm_list = CommList_DM3068
        self.meas = Meas(self, self._comm_list)




if __name__ == '__main__':
    multik = DM3068('address')
    with multik:
        print(multik.meas.voltage_dc)
