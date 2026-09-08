from .base_multimeter import Multimeter, Meas, CommList

CommList_DM3068 = CommList(
    voltage_dc = ':MEAS:VOLT:DC?',
    voltage_ac = ':MEAS:VOLT:AC?',
    current_dc = ':MEAS:CURR:DC?',
    current_ac = ':MEAS:CURR:AC?',
    resistance = ':MEAS:RES?',
    frequency = ':MEAS:FREQ?',
    capacitance = ':MEAS:CAP?',
    continuity = ':MEAS:CONT?',
    diode = ':MEAS:DIOD?',
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
