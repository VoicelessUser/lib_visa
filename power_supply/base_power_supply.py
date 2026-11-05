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

    ask_mode:str
    answer_CC: str
    answer_CV: str
    answer_UR: str


@dataclass
class DeviceSpecs:
    max_time_wait: float
    delay: float
    channel_tolerance: float
    num_channels: int = 3


def _check_channel_exists(num_channel: int, num_channels: int) -> None:
    """channel_1..3 создаются всегда (ради подсказок IDE), поэтому обращение
    к «лишнему» каналу прибора ловим здесь — иначе его команды без {channel}
    молча уйдут в реальный выход."""
    if num_channel > num_channels:
        raise ValueError(
            f'Канал {num_channel} не существует: у прибора {num_channels} кан.'
        )


class SetChannel:
    def __init__(self, num_channel: int, device: VisaComp, comm_list: CommList,
                 specs: DeviceSpecs):
        self._num_channel = num_channel
        self._device = device
        self._comm_list = comm_list
        self._num_channels = specs.num_channels

    @property
    def voltage(self) -> float:
        _check_channel_exists(self._num_channel, self._num_channels)
        return float(self._device._ask_parameter(self._comm_list.ask_voltage.format(channel=self._num_channel)))

    @voltage.setter
    def voltage(self, voltage_V: float):
        _check_channel_exists(self._num_channel, self._num_channels)
        self._device._set_parameter(self._comm_list.set_voltage.format(channel=self._num_channel, voltage_V=voltage_V))

    @property
    def current_limit(self) -> float:
        _check_channel_exists(self._num_channel, self._num_channels)
        return float(self._device._ask_parameter(self._comm_list.ask_current_limit.format(channel=self._num_channel)))

    @current_limit.setter
    def current_limit(self, curr_lim_A: float):
        _check_channel_exists(self._num_channel, self._num_channels)
        self._device._set_parameter(
            self._comm_list.set_current_limit.format(channel=self._num_channel, curr_lim_A=curr_lim_A))


class MeasChannel:
    def __init__(self, num_channel: int, device: VisaComp, comm_list: CommList,
                 specs: DeviceSpecs):
        self._num_channel = num_channel
        self._device = device
        self._comm_list = comm_list
        self._num_channels = specs.num_channels

    @property
    def current(self) -> float:
        _check_channel_exists(self._num_channel, self._num_channels)
        return float(self._device._ask_parameter(self._comm_list.meas_current.format(channel=self._num_channel)))

    @property
    def voltage(self) -> float:
        _check_channel_exists(self._num_channel, self._num_channels)
        return float(self._device._ask_parameter(self._comm_list.meas_voltage.format(channel=self._num_channel)))


class Channel:
    def __init__(self, num_channel: int, device: VisaComp, comm_list: CommList, specs: DeviceSpecs):
        self._max_time_wait = specs.max_time_wait
        self._delay = specs.delay
        self._channel_tolerance = specs.channel_tolerance
        self._num_channels = specs.num_channels
        self.num_channel = num_channel
        self._device = device

        self._comm_list = comm_list
        self.meas = MeasChannel(num_channel, device, comm_list, specs)
        self.set = SetChannel(num_channel, device, comm_list, specs)

    @property
    def state(self) -> bool:
        _check_channel_exists(self.num_channel, self._num_channels)
        answer = self._device._ask_parameter(
            self._comm_list.ask_state.format(channel=self.num_channel)
        ).strip().upper()
        return answer in ('1', 'ON')

    def on(self):
        _check_channel_exists(self.num_channel, self._num_channels)
        self._device._set_parameter(self._comm_list.set_on.format(channel=self.num_channel))

    def off(self):
        _check_channel_exists(self.num_channel, self._num_channels)
        self._device._set_parameter(self._comm_list.set_off.format(channel=self.num_channel))

    def wait_for_target_voltage(self, target_voltage: float):
        _check_channel_exists(self.num_channel, self._num_channels)
        """Ожидает установления целевого напряжения.

        Если answer_CC задан — определяет режим по ask_mode (CV/CC/UR).
        Если answer_CC пустой — проверяет КЗ по току относительно current_limit
        (логика TH6400).
        """
        # Перед первым опросом пауза: приборы применяют уставку с фирмварной
        # задержкой (замерено на DP832A: ~0.3–0.6 с на включение выхода и на
        # смену напряжения), опрашивать раньше бессмысленно. Плотный опрос
        # эту задержку ещё и растягивает (на DP832A при ~700 запросов/с
        # применение зависало до 2–8 с), поэтому delay не уплотнять.
        sleep(0.3)
        if self._comm_list.answer_CC:
            self._wait_by_mode(target_voltage)
        else:
            self._wait_by_current_limit(target_voltage)

    def _wait_by_mode(self, target_voltage: float):
        for _ in range(int(self._max_time_wait / self._delay)):
            mode = self._device._ask_parameter(self._comm_list.ask_mode.format(channel=self.num_channel)).strip()
            
            if mode == self._comm_list.answer_CV or mode == self._comm_list.answer_UR:
                actual_voltage = self.meas.voltage
                if target_voltage != 0:
                    if abs(target_voltage - actual_voltage) / target_voltage < self._channel_tolerance:
                        break
                else:
                    if  actual_voltage < self._channel_tolerance:
                        break
                    
            elif mode == self._comm_list.answer_CC:
                self.off()
                self._device.logger.error(f'Канал {self.num_channel} коротит')
                raise RuntimeError(f'Канал {self.num_channel} коротит (CC)')
                
            else:
                self._device.logger.error(f'Канал {self.num_channel} неизвестный режим: {mode}')
                raise ConnectionError(f'Канал {self.num_channel} в режиме {mode}')
            
            sleep(self._delay)  # ← ЗАДЕРЖКА

    def _wait_by_current_limit(self, target_voltage: float):
        """Ожидает установления целевого напряжения с проверкой на КЗ (CC) по току."""
        current_limit = self.set.current_limit

        for _ in range(int(self._max_time_wait / self._delay)):
            actual_voltage = self.meas.voltage
            actual_current = self.meas.current

            # Режим CC: ток близок к лимиту → короткое замыкание
            if actual_current >= current_limit * 0.95:
                self.off()
                self._device.logger.error(f'Канал {self.num_channel} коротит (CC)')
                raise RuntimeError(f'Канал {self.num_channel} коротит (CC)')

            # Режим CV: напряжение в пределах допуска
            if target_voltage == 0:
                if abs(actual_voltage) < self._channel_tolerance:
                    break
            else:
                if abs(target_voltage - actual_voltage) / target_voltage < self._channel_tolerance:
                    break

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


        

class BasePowerSupply(VisaComp):
    def __init__(self, port: str, comm_list: CommList, specs: DeviceSpecs,
                 channel_cls: type[Channel] = Channel):
        super().__init__(port)
        self._comm_list = comm_list
        self._specs = specs

        # Каналы создаются явными атрибутами, а не в цикле: только явные
        # атрибуты автодополняются IDE (ps.channel_1.set.voltage). Поэтому у
        # приборов с меньшим числом каналов channel_2/channel_3 существуют,
        # но при обращении падают с понятной ошибкой (см. _check_channel_exists).
        self.channel_1 = channel_cls(num_channel=1, device=self, comm_list=comm_list, specs=specs)
        self.channel_2 = channel_cls(num_channel=2, device=self, comm_list=comm_list, specs=specs)
        self.channel_3 = channel_cls(num_channel=3, device=self, comm_list=comm_list, specs=specs)
        # В channels — только реально существующие каналы прибора:
        # групповые операции (all_channels_off, set_all_channels)
        # «лишние» каналы не трогают.
        self.channels: tuple[Channel] = (
            self.channel_1, self.channel_2, self.channel_3,
        )[:specs.num_channels]

    def all_channels_off(self):
        for channel in self.channels:
            channel.off()

            
    def set_all_channels(self, voltage:list[float], current_limit:list[float]):
        if  not (len(voltage) == len(current_limit) == len(self.channels)):
            raise ValueError('voltage, channels and current_limit must be equal length')
        for channel, volt, curr_limit in zip(self.channels, voltage, current_limit):
            channel.set.voltage = volt
            channel.set.current_limit = curr_limit

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.all_channels_off()
        self.disconnect()
