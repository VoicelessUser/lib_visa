from .base_multimeter import BaseMultimeter, CommList, Measurement

# DM3068: сама команда измерения переводит прибор в нужный режим,
# поэтому config/mode_id пустые — переключение режима не требуется.
# Триггер и настройка вынесены в setup и отправляются перед каждым чтением.
CommList_DM3068 = CommList(
    setup=(':TRIG:COUN 1;:MEAS AUTO',),
    voltage_dc=Measurement(read=':MEAS:VOLT:DC?'),
    voltage_ac=Measurement(read=':MEAS:VOLT:AC?'),
    current_dc=Measurement(read=':MEAS:CURR:DC?'),
    current_ac=Measurement(read=':MEAS:CURR:AC?'),
    resistance=Measurement(read=':MEAS:RES?'),
    frequency=Measurement(read=':MEAS:FREQ?'),
    capacitance=Measurement(read=':MEAS:CAP?'),
    continuity=Measurement(read=':MEAS:CONT?'),
    diode=Measurement(read=':MEAS:DIOD?'),
    temperature=Measurement()
)


class DM3068(BaseMultimeter):
    _comm_list = CommList_DM3068


if __name__ == '__main__':
    multik = DM3068('address')
    with multik:
        print(multik.meas.voltage_dc)
