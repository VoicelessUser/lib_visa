from ..base_classes import VisaComp
from time import sleep
from dataclasses import dataclass


@dataclass
class CommList:
    # Функция канала: источник напряжения (CV) или источник тока (CC)
    set_mode_cv: str
    set_mode_cc: str
    ask_mode: str
    answer_CV: str    # ответ ask_mode в режиме источника напряжения ('VOLT')
    answer_CC: str    # ответ ask_mode в режиме источника тока ('CURR')

    # Уставка источника (активна половина, выбранная mode)
    set_voltage: str
    ask_voltage: str
    set_current: str
    ask_current: str

    # Лимит (compliance) противоположной величины:
    #   CV: limit.current, CC: limit.voltage
    set_i_limit: str
    ask_i_limit: str
    set_v_limit: str
    ask_v_limit: str

    # Измерения
    meas_voltage: str
    meas_current: str

    # Выход канала
    ask_state: str
    set_on: str
    set_off: str

    meas_resistance: str = None   # опционально (пусто — прибор не умеет)


@dataclass
class DeviceSpecs:
    max_time_wait: float
    delay: float
    tolerance: float
    num_channels: int = 1


def _check_channel_exists(num_channel: int, num_channels: int) -> None:
    """channel_1/channel_2 создаются всегда (ради подсказок IDE), поэтому
    обращение к «лишнему» каналу ловим здесь — иначе его команды уйдут
    в несуществующий канал прибора."""
    if num_channel > num_channels:
        raise ValueError(
            f'Канал {num_channel} не существует: у прибора {num_channels} кан.'
        )


class Mode:
    """Функция канала: источник напряжения (CV) или источник тока (CC).

    cv() — источаем напряжение, лимитируется ток (limit.current).
    cc() — источаем ток, лимитируется напряжение (limit.voltage).
    """

    def __init__(self, num_channel: int, device: VisaComp, comm_list: CommList,
                 num_channels: int):
        self._num_channel = num_channel
        self._device = device
        self._comm_list = comm_list
        self._num_channels = num_channels

    def cv(self):
        """Режим источника напряжения."""
        _check_channel_exists(self._num_channel, self._num_channels)
        self._device._set_parameter(
            self._comm_list.set_mode_cv.format(channel=self._num_channel))

    def cc(self):
        """Режим источника тока."""
        _check_channel_exists(self._num_channel, self._num_channels)
        self._device._set_parameter(
            self._comm_list.set_mode_cc.format(channel=self._num_channel))

    def ask(self) -> str:
        """Текущая функция канала: 'CV' либо 'CC'."""
        _check_channel_exists(self._num_channel, self._num_channels)
        answer = self._device._ask_parameter(
            self._comm_list.ask_mode.format(channel=self._num_channel)
        ).strip()

        if answer == self._comm_list.answer_CV:
            return 'CV'
        if answer == self._comm_list.answer_CC:
            return 'CC'

        self._device.logger.error(
            f'Канал {self._num_channel}: неизвестный режим: {answer}')
        raise ConnectionError(f'Канал {self._num_channel} в режиме {answer}')


class SetChannel:
    """Уставка источника. Активная величина определяется mode канала:
    в CV — voltage, в CC — current."""

    def __init__(self, num_channel: int, device: VisaComp, comm_list: CommList,
                 num_channels: int):
        self._num_channel = num_channel
        self._device = device
        self._comm_list = comm_list
        self._num_channels = num_channels

    @property
    def voltage(self) -> float:
        _check_channel_exists(self._num_channel, self._num_channels)
        return float(self._device._ask_parameter(
            self._comm_list.ask_voltage.format(channel=self._num_channel)))

    @voltage.setter
    def voltage(self, voltage_V: float):
        _check_channel_exists(self._num_channel, self._num_channels)
        self._device._set_parameter(self._comm_list.set_voltage.format(
            channel=self._num_channel, voltage_V=voltage_V))

    @property
    def current(self) -> float:
        _check_channel_exists(self._num_channel, self._num_channels)
        return float(self._device._ask_parameter(
            self._comm_list.ask_current.format(channel=self._num_channel)))

    @current.setter
    def current(self, curr_A: float):
        _check_channel_exists(self._num_channel, self._num_channels)
        self._device._set_parameter(self._comm_list.set_current.format(
            channel=self._num_channel, curr_A=curr_A))


class LimitChannel:
    """Лимит (compliance) противоположной величины:
    в CV ограничивается ток, в CC — напряжение."""

    def __init__(self, num_channel: int, device: VisaComp, comm_list: CommList,
                 num_channels: int):
        self._num_channel = num_channel
        self._device = device
        self._comm_list = comm_list
        self._num_channels = num_channels

    @property
    def current(self) -> float:
        _check_channel_exists(self._num_channel, self._num_channels)
        return float(self._device._ask_parameter(
            self._comm_list.ask_i_limit.format(channel=self._num_channel)))

    @current.setter
    def current(self, curr_lim_A: float):
        _check_channel_exists(self._num_channel, self._num_channels)
        self._device._set_parameter(self._comm_list.set_i_limit.format(
            channel=self._num_channel, curr_lim_A=curr_lim_A))

    @property
    def voltage(self) -> float:
        _check_channel_exists(self._num_channel, self._num_channels)
        return float(self._device._ask_parameter(
            self._comm_list.ask_v_limit.format(channel=self._num_channel)))

    @voltage.setter
    def voltage(self, volt_lim_V: float):
        _check_channel_exists(self._num_channel, self._num_channels)
        self._device._set_parameter(self._comm_list.set_v_limit.format(
            channel=self._num_channel, volt_lim_V=volt_lim_V))


class MeasChannel:
    def __init__(self, num_channel: int, device: VisaComp, comm_list: CommList,
                 num_channels: int):
        self._num_channel = num_channel
        self._device = device
        self._comm_list = comm_list
        self._num_channels = num_channels

    @property
    def voltage(self) -> float:
        _check_channel_exists(self._num_channel, self._num_channels)
        return float(self._device._ask_parameter(
            self._comm_list.meas_voltage.format(channel=self._num_channel)))

    @property
    def current(self) -> float:
        _check_channel_exists(self._num_channel, self._num_channels)
        return float(self._device._ask_parameter(
            self._comm_list.meas_current.format(channel=self._num_channel)))

    @property
    def resistance(self) -> float:
        if self._comm_list.meas_resistance is None:
            raise NotImplementedError(
                'Измерение сопротивления не задано в CommList прибора')
        _check_channel_exists(self._num_channel, self._num_channels)
        return float(self._device._ask_parameter(
            self._comm_list.meas_resistance.format(channel=self._num_channel)))


class Channel:
    def __init__(self, num_channel: int, device: VisaComp, comm_list: CommList,
                 specs: DeviceSpecs):
        self._max_time_wait = specs.max_time_wait
        self._delay = specs.delay
        self._tolerance = specs.tolerance
        self._num_channels = specs.num_channels
        self.num_channel = num_channel
        self._device = device
        self._comm_list = comm_list

        self.mode = Mode(num_channel, device, comm_list, specs.num_channels)
        self.set = SetChannel(num_channel, device, comm_list, specs.num_channels)
        self.limit = LimitChannel(num_channel, device, comm_list, specs.num_channels)
        self.meas = MeasChannel(num_channel, device, comm_list, specs.num_channels)

    @property
    def state(self) -> bool:
        _check_channel_exists(self.num_channel, self._num_channels)
        answer = self._device._ask_parameter(
            self._comm_list.ask_state.format(channel=self.num_channel)
        ).strip().upper()
        return answer in ('1', 'ON')

    def on(self):
        _check_channel_exists(self.num_channel, self._num_channels)
        self._device._set_parameter(
            self._comm_list.set_on.format(channel=self.num_channel))

    def off(self):
        _check_channel_exists(self.num_channel, self._num_channels)
        self._device._set_parameter(
            self._comm_list.set_off.format(channel=self.num_channel))

    def wait_for_target(self):
        """Ожидает установления активной величины (V в CV, I в CC).

        Compliance: если пассивная величина достигла лимита (0.95 от него)
        — выключает выход и бросает ошибку: в CV это КЗ, в CC — обрыв/нет
        нагрузки.
        """
        _check_channel_exists(self.num_channel, self._num_channels)
        mode = self.mode.ask()

        if mode == 'CV':
            target = self.set.voltage
            limit = abs(self.limit.current)
        else:
            target = self.set.current
            limit = abs(self.limit.voltage)

        for _ in range(int(self._max_time_wait / self._delay)):
            if mode == 'CV':
                actual = self.meas.voltage
                passive = abs(self.meas.current)
            else:
                actual = self.meas.current
                passive = abs(self.meas.voltage)

            if limit > 0 and passive >= limit * 0.95:
                self.off()
                fault = 'КЗ' if mode == 'CV' else 'обрыв / нет нагрузки'
                msg = f'Канал {self.num_channel} в compliance ({mode}): {fault}'
                self._device.logger.error(msg)
                raise RuntimeError(msg)

            if target == 0:
                if abs(actual) < self._tolerance:
                    break
            elif abs(target - actual) / abs(target) < self._tolerance:
                break

            sleep(self._delay)

    def safe_on(self):
        """Включает выход с мягким стартом: 20% уставки -> ожидание -> полная
        уставка. В CV ramp по напряжению, в CC — по току."""
        _check_channel_exists(self.num_channel, self._num_channels)
        mode = self.mode.ask()

        if mode == 'CV':
            target = self.set.voltage
            # Этап 1: soft-start на 20%
            self.set.voltage = target / 5
            self.on()
            self.wait_for_target()
            # Этап 2: полная уставка
            self.set.voltage = target
            self.wait_for_target()
        else:
            target = self.set.current
            self.set.current = target / 5
            self.on()
            self.wait_for_target()
            self.set.current = target
            self.wait_for_target()


class BaseSourceMeter(VisaComp):
    def __init__(self, port: str, comm_list: CommList, specs: DeviceSpecs,
                 channel_cls: type[Channel] = Channel):
        super().__init__(port)
        self._comm_list = comm_list
        self._specs = specs

        # Каналы создаются явными атрибутами, а не в цикле: только явные
        # атрибуты автодополняются IDE (smu.channel_1.set.voltage). Поэтому у
        # одноканальных приборов channel_2 существует, но при обращении падает
        # с понятной ошибкой (см. _check_channel_exists).
        self.channel_1 = channel_cls(num_channel=1, device=self, comm_list=comm_list, specs=specs)
        self.channel_2 = channel_cls(num_channel=2, device=self, comm_list=comm_list, specs=specs)
        # В channels — только реально существующие каналы прибора:
        # групповые операции (all_channels_off) «лишние» каналы не трогают.
        self.channels: tuple[Channel] = (
            self.channel_1, self.channel_2,
        )[:specs.num_channels]

    def all_channels_off(self):
        for channel in self.channels:
            channel.off()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.all_channels_off()
        self.disconnect()
