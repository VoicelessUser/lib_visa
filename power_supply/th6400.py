from .base_power_supply import CommList, DeviceSpecs, PowerSupply, Channel
from time import sleep

'''Акип 1181/3'''

th6400_commands = CommList(
    set_voltage="INST:NSEL {channel};VOLT {voltage_V}",
    ask_voltage="INST:NSEL {channel};VOLT?",
    set_current_limit="INST:NSEL {channel};CURR {curr_lim_A}",
    ask_current_limit="INST:NSEL {channel};CURR?",

    meas_current="INST:NSEL {channel};MEAS:CURR?",
    meas_voltage="INST:NSEL {channel};MEAS:VOLT?",

    ask_state="INST:NSEL {channel};OUTP?",
    set_on="INST:NSEL {channel};OUTP ON",
    set_off="INST:NSEL {channel};OUTP OFF",
    ask_mode='',  # не используется в TH6400
    answer_CC='CC',
    answer_CV='CV',
    answer_UR= 'UR'
)

th6400_specs = DeviceSpecs(
    num_channels=3,
    max_time_wait=2.0,
    delay=0.05,
    channel_tolerance=0.02
)


class TH6400Channel(Channel):
    def wait_for_target_voltage(self, target_voltage: float):
        """Ожидает установления целевого напряжения с проверкой на КЗ (CC)."""
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


class TH6400(PowerSupply):
    def __init__(self, port: str = ''):
        super().__init__(port, th6400_commands, th6400_specs, channel_cls=TH6400Channel)


if __name__ == "__main__":
    ps = TH6400('USB0::42560::25600::DC51250102::0::INSTR')
    # Пример строки подключения для USB CDC (COM-порт):
    # ps.port = 'ASRL3::INSTR'
    # Пример для USB TMC:
    # ps.port = 'USB0::0xXXXX::0xXXXX::TH6400XXXX::INSTR'
    with ps:
        ps.channel_1.set.voltage = 1
        ps.channel_1.safe_on()
