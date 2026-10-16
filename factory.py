"""Единая фабрика приборов: имя + адрес -> экземпляр прибора.

    from lib_visa import get_device

    ps = get_device('DP832A', 'USB0::0x1AB1::0x0E11::DP8B262201226::INSTR')
    ps = get_device('PowerSupplyTest', 'test')   # виртуальный прибор

Имя нечувствительно к регистру. Неизвестное имя бросает ValueError
со списком доступных.
"""

from .power_supply import DP832A, NGE100, AKIP1143, TH6400, PowerSupplyTest
from .multimeter import DM3068, AKIP2101, SDM3045X, MultimeterTest
from .sourse_meter import Keithley2461, SourceMeterTest
from .load import DL3021A, PEL500, LoadTest
from .lcr import E4980, LcrTest

_DEVICES = {
    # Источники питания
    'DP832A': DP832A,
    'DP832': DP832A,
    'NGE100': NGE100,
    'AKIP1143': AKIP1143,
    'TH6400': TH6400,
    'POWERSUPPLYTEST': PowerSupplyTest,

    # Мультиметры
    'DM3068': DM3068,
    'AKIP2101': AKIP2101,
    'SDM3045X': SDM3045X,
    'SDM3045': SDM3045X,
    'MULTIMETERTEST': MultimeterTest,

    # Сурсметры
    'KEITHLEY2461': Keithley2461,
    'KEITHLEY 2461': Keithley2461,
    '2461': Keithley2461,
    'SOURCEMETERTEST': SourceMeterTest,

    # Электронные нагрузки
    'DL3021A': DL3021A,
    'PEL500': PEL500,
    'LOADTEST': LoadTest,

    # LCR-метры
    'E4980': E4980,
    'LCRTEST': LcrTest,
}


def get_device(name: str, port: str):
    """Возвращает экземпляр прибора по имени модели и адресу порта.

    get_device('DP832A', 'USB0::...')  — реальный прибор
    get_device('PowerSupplyTest', 'test')  — виртуальный тестовый прибор
    """
    key = name.strip().upper()
    try:
        device_cls = _DEVICES[key]
    except KeyError:
        raise ValueError(
            f"Unknown device '{name}'. Available: {sorted(_DEVICES)}"
        ) from None
    return device_cls(port)
