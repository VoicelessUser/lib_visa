from ..base_classes import VisaComp
class DL3021A(VisaComp):

    def __init__(self, port: str = ''):
        super().__init__(port)

    def load_on(self):
        message = f":SOUR:INP:STAT 1\r"
        self._set_parameter(message)
        return self

    def load_off(self):
        message = f":SOUR:INP:STAT 0\r"
        self._set_parameter(message)
        return self

    def read_volt(self)->float:
        message = f":MEASure:VOLTage?\r"
        return float(self._ask_parameter(message))

    def set_curr(self, curr: float):
        message = f":SOUR:CURR {curr}\r"
        self._set_parameter(message)
        return self

    def set_res(self, load_resistance_ohm: float):
        message = f':SOUR:RES:LEV:IMM {load_resistance_ohm}'
        self._set_parameter(message)
        return self

if __name__ == '__main__':
    load = DL3021A()
    load.port = ''
    try:
        load.connec()
        load.load_on().set_curr(0.5)
        print(load.read_volt())
        load.load_off()
    finally:
        load.disconnect()