# serial.tools.list_ports_common      Replaced in code for simplicity
# serial.tools.list_ports             Done
# serial.serial_for_url               Done
# serial.SerialException              Done
# serial.serialutil.SerialException   Done

# from serial.tools.list_ports_common import ListPortInfo
# import serial.tools.list_ports as list_ports

# self._port.open()                   Done
# self._port.rts
# self._port.dtr
# self._port.write_timeout
# self._port.close()                  Done
# self._port.port
# self._port.baudrate
# self._port.write()
# self._port.timeout
# self._port.read()
# self._port.flushInput()
# self._port.reset_input_buffer()
# self._port.inWaiting()
# self._port.flushOutput()
# self._port.name # mainly for usb-to-serial, might not be necessary, it will always evaluate to true  loader.py line 743

# Functions that _port is passed to (to check)
slip_reader
CustomReset
USBJTAGSerialReset
UnixTightReset
ClassicReset
HardReset

from .reset import (
    ClassicReset,
    CustomReset,
    # DEFAULT_RESET_DELAY,   not relevant
    HardReset,
    USBJTAGSerialReset,
    UnixTightReset,
)

# Always traces to
class ResetStrategy

# self.port.open()  Already seen above

self.port.isOpen()

# self.port.close()  Already seen above

self.port.setRTS()

self.port.setDTR()

self.port.fileno
