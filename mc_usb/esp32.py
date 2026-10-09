from dataclasses import dataclass
from typing import Optional
import serial
import time
import logging
from math import log


@dataclass(frozen=True)
class ESP32Commands:
    par = 'par{group}:{pins_state}'
    spi = 'spi:{cs_state_for_write}_{data}'
    cs = 'cs:{cs_state}'
    get_pin_state = 'get:{group}'


class ESP32Par:
    """Класс для управления параллельными портами ESP32"""
    
    def __init__(self, communicator: 'ESP32Comm'):
        self._comm = communicator
        self._cmd = ESP32Commands()
        self._group_pin_quantity = [4,6]
    
    def _set_states(self, group: int, states: list[bool]) -> str:
        if len(states) != self._group_pin_quantity[group]:
            raise RuntimeError(
                f'ESP32: для group {group} ожидается {self._group_pin_quantity[group]} '
                f'состояний пинов, получено {len(states)}'
            )
        pin_state_list_str = ''.join(['1' if state else '0' for state in states])
        command = self._cmd.par.format(group=group, pins_state=pin_state_list_str)
        answer = self._comm.send_command(command)
        return answer
    
    def _check_pin_number(self, group:int, pin_list: list[int]) -> bool:
        match = (max(pin_list) < self._group_pin_quantity[group]) and len(pin_list) < self._group_pin_quantity[group]
        if not match:
            raise ValueError(f'Invalid pin number for group {group}')
        return match

    def _build_pin_state_list(self, group: int, pin_list: list[int], value:bool) -> list[bool]:
        self._check_pin_number(group, pin_list)
        pin_state_list = [False] * self._group_pin_quantity[group]
        for pin in range(self._group_pin_quantity[group]):
            if pin in pin_list:
                pin_state_list[pin] = value
            else:
                pin_state_list[pin] = not value
        return pin_state_list
    
    def set_state_cs(self, cs_state:bool)->str:
        answer = self._comm.send_command(self._cmd.cs.format(cs_state=int(cs_state)))
        return answer

    def get_pin_state(self, group: int, retries: int = 5) -> list[bool]:
        """Get pin state"""
        command = self._cmd.get_pin_state.format(group=group)
        answer = ''
        for _ in range(retries):
            answer = self._comm.send_command(command)
            # ESP32 может писать в порт отладочный спам — ищем среди строк
            # единственную валидную: ровно N значений 0/1 через запятую
            for line in answer.splitlines():
                tokens = [token.strip() for token in line.split(',')]
                if len(tokens) == self._group_pin_quantity[group] and all(t in ('0', '1') for t in tokens):
                    return [t == '1' for t in tokens]
        raise RuntimeError(
            f'ESP32: не удалось прочитать состояние пинов group {group}. '
            f'Последний ответ: {answer!r}'
        )
    
    def set_pins_r(self, group: int, pin_list: list[int], state: bool) -> str:
        """Reset another"""
        pin_state_list = self._build_pin_state_list(group, pin_list, state)
        return self._set_states(group, pin_state_list)

    def set_pins_all(self, group: int, state: bool) -> str:
        """Reset all"""
        pin_state_list = [state] * self._group_pin_quantity[group]
        return self._set_states(group, pin_state_list)
    
    def set_pins_k(self, group: int, pin_list: list[int], state: bool) -> str:
        """keep state another"""
        self._check_pin_number(group, pin_list)
        actual_state = self.get_pin_state(group)
        new_state = actual_state.copy()
        for pin in pin_list:
            new_state[pin] = state
        return self._set_states(group, new_state)
    
    def send_mail(self, group: int, mail: int, cs_state_for_write: bool= False) -> str:
        """Хуйню придумал удали или разчлени потом"""
        group_size = self._group_pin_quantity[group]
        if 2**group_size <= mail:
            raise ValueError(f'Too big mail for group {group}')
        pin_list = [bool((mail >> i) & 1) for i in range(group_size)]

        self.set_state_cs(cs_state_for_write)
        answer =self._set_states(group, pin_list)
        self.set_state_cs(not cs_state_for_write)
        return answer

        

class ESP32Spi:
    """Класс для управления SPI ESP32"""
    
    def __init__(self, communicator: 'ESP32Comm'):
        self._comm = communicator
        self._cmd = ESP32Commands()
    
    def write(self, mail: int, cs_state_for_write:bool= False) -> str:
        cs_state_for_write = int(cs_state_for_write)
        return self._comm.send_command(self._cmd.spi.format(data=mail, cs_state_for_write=cs_state_for_write))


class ESP32Comm:
    """Основной класс для работы с ESP32 через Serial"""

    MAX_SEND_ATTEMPTS = 3

    def __init__(self, port: str, baudrate: int = 115200, timeout: float = 1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self._serial: Optional[serial.Serial] = None
        self.logger = logging.getLogger("hw")
        
        self.par = ESP32Par(self)
        self.spi = ESP32Spi(self)

    def connect(self) -> bool:
        try:
            self._serial = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )
            time.sleep(0.1)
            self._serial.reset_input_buffer()
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False
    
    def disconnect(self) -> bool:
        if self._serial and self._serial.is_open:
            self._serial.close()
            return True
        return False
    
    def send_command(self, command: str) -> str:
        if not self._serial or not self._serial.is_open:
            return "Error: not connected"
        
        answer = self._simple_send_command(command)

        attempts = 0
        while "ERR" in answer or "Err" in answer:
            attempts += 1
            if attempts >= self.MAX_SEND_ATTEMPTS:
                # Отдаём последний ответ (с ошибкой) вызывающему коду,
                # управление возвращается всегда — без бесконечного цикла.
                return answer
            time.sleep(0.1)
            answer = self._simple_send_command(command)
        return answer
        
    def _simple_send_command(self, command:str) -> str:
        self._serial.write(f"{command}\n".encode())
        self._serial.flush()

        response_lines = []
        start_time = time.time()
        while time.time() - start_time < self.timeout:
            if self._serial.in_waiting:
                line = self._serial.readline().decode().strip()
                if line:
                    response_lines.append(line)
                    if not self._serial.in_waiting:
                        break
        self.logger.info(f"Send: {command}, Response: {response_lines}")
        time.sleep(0.1)
        return "\n".join(response_lines) if response_lines else "Error: no response"
    
    
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()


if __name__ == "__main__":
    esp = ESP32Comm(port='COM16')
    
    with esp:
        # Тест state_only
        print(esp.par.send_mail(mail=63, cs_state_for_write=False, group=1))
        time.sleep(0.1)
        print(esp.par.send_mail(mail=0, cs_state_for_write=False, group=1))
        time.sleep(0.1)
