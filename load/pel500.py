from ..base_classes import SerialComp

class PEL500Mode:
    """Mode control for PEL500 electronic load."""

    def __init__(self, device:SerialComp):
        self._device = device

    def cc(self):
        """Set constant current mode."""
        self._device._set_parameter("MODE CC")
        return self

    def cr(self):
        """Set constant resistance mode."""
        self._device._set_parameter("MODE CR")
        return self

    def cv(self):
        """Set constant voltage mode."""
        self._device._set_parameter("MODE CV")
        return self

    def cp(self):
        """Set constant power mode."""
        self._device._set_parameter("MODE CP")
        return self

    @property
    def get(self) -> str:
        """Returns current mode: 'CC', 'CR', 'CV', 'CP'."""
        mapping = {"0": "CC", "1": "CR", "2": "CV", "3": "CP"}
        return mapping.get(self._device._ask_parameter("MODE?"), "UNKNOWN")


class PEL500Conf:
    """Configuration (voltage, current, resistance, power settings) for PEL500."""

    def __init__(self, device:SerialComp):
        self._device = device
        self.current = PEL500ConfLevel(device, "CURR")
        self.voltage = PEL500ConfLevel(device, "CV")
        self.power = PEL500ConfLevel(device, "CP")
        self.resistance = PEL500ConfLevel(device, "CR")


class PEL500ConfLevel:
    """Configuration level (HIGH/LOW) for current, voltage, power, resistance."""

    def __init__(self, device:SerialComp, param_prefix: str):
        self._device = device
        self._prefix = param_prefix

    @property
    def high(self) -> float:
        return float(self._device._ask_parameter(f"{self._prefix}:HIGH?"))

    @high.setter
    def high(self, value: float):
        self._device._set_parameter(f"{self._prefix}:HIGH {value}")

    @property
    def low(self) -> float:
        return float(self._device._ask_parameter(f"{self._prefix}:LOW?"))

    @low.setter
    def low(self, value: float):
        self._device._set_parameter(f"{self._prefix}:LOW {value}")


class PEL500Meas:
    """Measurements for PEL500 electronic load."""

    def __init__(self, device:SerialComp):
        self._device = device

    @property
    def current(self) -> float:
        return float(self._device._ask_parameter("MEAS:CURR?"))

    @property
    def voltage(self) -> float:
        return float(self._device._ask_parameter("MEAS:VOLT?"))

    @property
    def power(self) -> float:
        return float(self._device._ask_parameter("MEAS:POW?"))


class PEL500Limits:
    """Limits configuration for PEL500 electronic load."""

    def __init__(self, device):
        self._device = device
        self.current = PEL500LimitsLevel(device, "I")
        self.voltage = PEL500LimitsLevel(device, "V")
        self.power = PEL500LimitsLevel(device, "W")


class PEL500LimitsLevel:
    """Limits level (HIGH/HIGH current, LOW/LOW current) for current, voltage, power."""

    def __init__(self, device:SerialComp, prefix: str):
        self._device = device
        self._prefix = prefix

    @property
    def high(self) -> float:
        return float(self._device._ask_parameter(f"{self._prefix}H?"))

    @high.setter
    def high(self, value: float):
        self._device._set_parameter(f"{self._prefix}H {value}")

    @property
    def low(self) -> float:
        return float(self._device._ask_parameter(f"{self._prefix}L?"))

    @low.setter
    def low(self, value: float):
        self._device._set_parameter(f"{self._prefix}L {value}")

class PEL500(SerialComp):
    """Electronic Load PEL-500 Series (GW Instek).
    
    Communicates via RS232/USB virtual COM port.
    Default baudrate: 115200, 8N1, RTS/CTS.
    Commands end with newline.
    """

    def __init__(self, port: str = ''):
        super().__init__(port, baudrate=115200, timeout=1.0)
        self.mode = PEL500Mode(self)
        self.conf = PEL500Conf(self)
        self.meas = PEL500Meas(self)
        self.limits = PEL500Limits(self)

    # --- Load state ---

    def load_on(self):
        self._set_parameter("LOAD ON")
        return self

    def load_off(self):
        self._set_parameter("LOAD OFF")
        return self

    @property
    def is_load_on(self) -> bool:
        return self._ask_parameter("LOAD?") == "1"

    # --- Short circuit ---

    def short_on(self):
        self._set_parameter("SHORT ON")
        return self

    def short_off(self):
        self._set_parameter("SHORT OFF")
        return self

    @property
    def is_short_on(self) -> bool:
        return self._ask_parameter("SHORT?") == "1"

    # --- Dynamic ---

    def set_dynamic(self, state: bool):
        self._set_parameter(f"DYN {'ON' if state else 'OFF'}")
        return self

    @property
    def is_dynamic_on(self) -> bool:
        return self._ask_parameter("DYN?") == "1"

    @property
    def level(self) -> str:
        return "HIGH" if self._ask_parameter("LEV?") == "1" else "LOW"

    @level.setter
    def level(self, value: str):
        self._set_parameter(f"LEV {value.upper()}")

    # --- Slew rate (A/uS) ---

    @property
    def rise_slew(self) -> float:
        return float(self._ask_parameter("RISE?"))

    @rise_slew.setter
    def rise_slew(self, value: float):
        self._set_parameter(f"RISE {value}")

    @property
    def fall_slew(self) -> float:
        return float(self._ask_parameter("FALL?"))

    @fall_slew.setter
    def fall_slew(self, value: float):
        self._set_parameter(f"FALL {value}")

    # --- Load ON/OFF voltage ---

    @property
    def load_on_voltage(self) -> float:
        return float(self._ask_parameter("LDONV?"))

    @load_on_voltage.setter
    def load_on_voltage(self, value: float):
        self._set_parameter(f"LDONV {value}")

    @property
    def load_off_voltage(self) -> float:
        return float(self._ask_parameter("LDOFFV?"))

    @load_off_voltage.setter
    def load_off_voltage(self, value: float):
        self._set_parameter(f"LDOFFV {value}")

    # --- System ---

    def remote(self):
        self._set_parameter("REMOTE")
        return self

    def local(self):
        self._set_parameter("LOCAL")
        return self

    def reset(self):
        self._set_parameter("*RST")
        return self

    def recall(self, state: int, bank: int = 1):
        self._set_parameter(f"RECALL {state},{bank}")
        return self

    def store(self, state: int, bank: int = 1):
        self._set_parameter(f"STORE {state},{bank}")
        return self

    @property
    def error(self) -> str:
        return self._ask_parameter("ERROR?")

    def clear_error(self):
        self._set_parameter("CLRERR")
        return self
