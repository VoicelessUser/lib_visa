# lib_visa

Python-библиотека для управления измерительными приборами по **VISA/SCPI** и **Serial**:
источники питания, электронные нагрузки, мультиметры, анализаторы цепей (VNA),
сурсметры, LCR-метры, анализаторы спектра и микроконтроллерные платы (ESP32).

Версия: 0.2.1 · Лицензия: MIT · Python ≥ 3.9

## Установка

```bash
pip install .
# или для разработки
pip install -e .[test]
```

Зависимости: `pyvisa`, `pyserial`, `PyYAML`, `numpy`, `scipy`.

Для работы VISA нужен бэкенд — **NI-VISA** (Windows/Linux x86) или **pyvisa-py**
(автоматически используется как fallback, а на ARM-Linux, например Raspberry Pi, — принудительно).

## Поддерживаемые приборы

| Категория | Класс | Прибор |
|---|---|---|
| Источники питания | `DP832A`, `NGE100`, `AKIP1143`, `TH6400` | Rigol DP832A, Rohde & Schwarz NGE100, АКИП-1143, Tek/Keithley TH6400 |
| Электронные нагрузки | `DL3021A`, `PEL500` | Rigol DL3021A (VISA), PEL500 (Serial) |
| Мультиметры | `DM3068`, `AKIP2101` | Rigol DM3068, АКИП-2101 |
| Сурсметры | `Keithley2461` | Keithley 2461 |
| LCR-метры | `E4980` | Keysight E4980A |
| Анализаторы цепей | `ZNB20` | Rohde & Schwarz ZNB20 |
| Анализаторы спектра | `MS2038C` | Anritsu MS2038C |
| МК-платы | `ESP32Comm` | ESP32 как коммутатор (параллельные порты + SPI) |

## Архитектура

```
lib_visa/
├── base_classes/
│   ├── visa_comp.py    # VisaComp — базовый VISA-коммуникатор (реконнект, ретраи, тест-режим)
│   ├── serial_comp.py  # SerialComp — базовый Serial-коммуникатор
│   └── search.py       # Сканирование VISA-ресурсов (*IDN?)
├── power_supply/       # PowerSupply + Channel/SetChannel/MeasChannel
├── sourse_meter/       # SourceMeter + Set/Meas
├── multimeter/         # Multimeter + Meas
├── load/, lcr/, vna/, spectrum_analyzer/, mc_usb/
└── all_ports.yaml      # Таблица VISA-адресов приборов стенда
```

Ключевая идея: команды SCPI не зашиты в коде классов, а вынесены в
датаклассы **`CommList`** / **`DeviceSpecs`** (шаблоны строк с `{channel}`,
`{voltage_V}` и т.п.). Драйвер нового прибора — это обычно одна команда:
подставить его SCPI-команды в `CommList` и унаследовать базовый класс категории.

### VisaComp / SerialComp

Общие возможности всех приборов:

- автоматический выбор VISA-бэкенда (NI-VISA → pyvisa-py);
- повторные попытки подключения и реконнект при обрыве связи;
- контекстный менеджер (`with`), гарантированный `disconnect()`;
- `identify_yourself()` → ответ на `*IDN?`;
- тест-режим без железа: порты `'test'` (строка/время), `'test_float'` (случайное число),
  `'test_list'` (случайный список чисел);
- логирование в логгер `hw` (`logging.getLogger("hw")`).

## Примеры использования

### Источник питания

```python
from lib_visa import DP832A

with DP832A('USB0::0x1AB1::0x0E11::DP8B262201226::INSTR') as ps:
    ps.channel_1.set.voltage = 3.3
    ps.channel_1.set.current_limit = 0.1
    ps.channel_1.safe_on()                 # soft-start на 20%, затем полное напряжение

    print(ps.channel_1.meas.voltage)       # измеренное напряжение
    print(ps.channel_1.meas.current)       # измеренный ток
    print(ps.channel_1.set.voltage)        # установленное напряжение
```

`safe_on()` ждёт выхода на целевое напряжение и отключает канал с ошибкой,
если прибор перешёл в режим CC (короткое замыкание). При выходе из `with`
все каналы принудительно выключаются (`all_channels_off()`).

```python
# Задать все три канала разом
ps.set_all_channels(voltage=[3.3, 5.0, 12.0], current_limit=[0.1, 0.5, 1.0])
```

### Мультиметр

```python
from lib_visa import DM3068

with DM3068('USB0::0x1AB1::0x0C94::DM3O274402192::INSTR') as mm:
    print(mm.meas.voltage_dc)
    print(mm.meas.resistance)
```

### Сурсметр

```python
from lib_visa import Keithley2461

with Keithley2461(port) as sm:
    sm.set.voltage = 5.0
    sm.set.current_limit = 0.01
    sm.safe_on()
    print(sm.meas.voltage, sm.meas.current)
```

### Анализатор цепей (VNA)

```python
from lib_visa import ZNB20

with ZNB20(port) as vna:
    vna.sweep_type.lin()
    vna.freq.set_range(1e6, 3e9)           # диапазон частот
    vna.sweep.set_points(1601)
    vna.power.set_source_power(chanel=1, power=-10)
    amp = vna.meas.amp_data(channel=1)     # данные трассы
    freqs = vna.meas.freq_data(channel=1)  # частоты точек
```

### Электронная нагрузка

```python
from lib_visa import DL3021A

with DL3021A(port) as load:
    load.set_curr(0.5)
    load.load_on()
    print(load.read_volt())
    load.load_off()
```

### LCR-метр

```python
from lib_visa import E4980

with E4980(port) as lcr:
    lcr.frequency = 1e6
    lcr.voltage = 0.5
    lcr.meas_type_capacitance.parallel_measurement()  # Cp-D, затем lcr.meas
    print(lcr.main_meas, lcr.side_meas)
```

### Поиск подключённых приборов

```bash
python -m lib_visa.base_classes.search
# или напрямую:
python base_classes/search.py
```

Скрипт выводит список VISA-ресурсов и ответ каждого на `*IDN?`.

### Тест-режим без железа

```python
ps = DP832A('test_float')
ps.connect()
print(ps.channel_1.meas.voltage)   # случайное float около 2.5
```

## Адреса приборов

VISA-адреса стенда хранятся в `all_ports.yaml`:

```python
import yaml
from lib_visa import DP832A

with open('all_ports.yaml') as f:
    ports = yaml.safe_load(f)

with DP832A(ports['DP832A']) as ps:
    ...
```

## Как добавить новый прибор

1. Скопируйте драйвер похожего прибора из соответствующей категории (например, `dp832a.py`).
2. Подставьте SCPI-команды вашего прибора в `CommList` (шаблоны с `{channel}`, `{voltage_V}` и т.д.).
3. При необходимости скорректируйте `DeviceSpecs` (`max_time_wait`, `delay`, `channel_tolerance`).
4. Добавьте класс в `__init__.py` соответствующего подпакета и корневой `__init__.py`.

## Тесты

```bash
pip install -e .[test]
pytest
```
