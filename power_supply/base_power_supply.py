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


class SetChannel:
    def __init__(self, num_channel: int, device: VisaComp, comm_list: CommList):
        self._num_channel = num_channel
        self._device = device
        self._comm_list = comm_list

    @property
    def voltage(self) -> float:
        return float(self._device._ask_parameter(self._comm_list.ask_voltage.format(channel=self._num_channel)))

    @voltage.setter
    def voltage(self, voltage_V: float):
        self._device._set_parameter(self._comm_list.set_voltage.format(channel=self._num_channel, voltage_V=voltage_V))

    @property
    def current_limit(self) -> float:
        return float(self._device._ask_parameter(self._comm_list.ask_current_limit.format(channel=self._num_channel)))

    @current_limit.setter
    def current_limit(self, curr_lim_A: float):
        self._device._set_parameter(
            self._comm_list.set_current_limit.format(channel=self._num_channel, curr_lim_A=curr_lim_A))


class MeasChannel:
    def __init__(self, num_channel: int, device: VisaComp, comm_list: CommList):
        self._num_channel = num_channel
        self._device = device
        self._comm_list = comm_list

    @property
    def current(self) -> float:
        return float(self._device._ask_parameter(self._comm_list.meas_current.format(channel=self._num_channel)))

    @property
    def voltage(self) -> float:
        return float(self._device._ask_parameter(self._comm_list.meas_voltage.format(channel=self._num_channel)))


class Channel:
    def __init__(self, num_channel: int, device: VisaComp, comm_list: CommList, specs: DeviceSpecs):
        self._max_time_wait = specs.max_time_wait
        self._delay = specs.delay
        self._channel_tolerance = specs.channel_tolerance
        self.num_channel = num_channel
        self._device = device

        self._comm_list = comm_list
        self.meas = MeasChannel(num_channel, device, comm_list)
        self.set = SetChannel(num_channel, device, comm_list)

    @property
    def state(self) -> bool:
        return bool(self._device._ask_parameter(self._comm_list.ask_state.format(channel=self.num_channel)))

    def on(self):
        self._device._set_parameter(self._comm_list.set_on.format(channel=self.num_channel))

    def off(self):
        self._device._set_parameter(self._comm_list.set_off.format(channel=self.num_channel))

    def wait_for_target_voltage(self, target_voltage: float):
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

    def safe_on(self):
        target_voltage = self.set.voltage
        
        # Этап 1: soft-start на 20%
        self.set.voltage = target_voltage / 5
        self.on()
        self.wait_for_target_voltage(target_voltage / 5)
        
        # Этап 2: полное напряжение
        self.set.voltage = target_voltage
        self.wait_for_target_voltage(target_voltage)


        

class PowerSupply(VisaComp):
    def __init__(self, port: str, comm_list: CommList, specs: DeviceSpecs,
                 channel_cls: type[Channel] = Channel):
        super().__init__(port)
        self._comm_list = comm_list
        self._specs = specs

        self.channel_1 = channel_cls(num_channel=1, device=self, comm_list=comm_list, specs=specs)
        self.channel_2 = channel_cls(num_channel=2, device=self, comm_list=comm_list, specs=specs)
        self.channel_3 = channel_cls(num_channel=3, device=self, comm_list=comm_list, specs=specs)
        self.channels: tuple[Channel] = (self.channel_1, self.channel_2, self.channel_3)

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
