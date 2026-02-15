# so a simple ``bytes(sequence)`` doesn't work for all versions
def to_bytes(seq):
    """convert a sequence to a bytes type"""
    if isinstance(seq, bytes):
        return seq
    elif isinstance(seq, bytearray):
        return bytes(seq)
    elif isinstance(seq, memoryview):
        return seq.tobytes()
    elif isinstance(seq, unicode):
        raise TypeError(
            "unicode strings are not supported, please encode to bytes: {!r}".format(
                seq
            )
        )
    else:
        # handle list of integers and bytes (one or more items) for Python 2 and 3
        return bytes(bytearray(seq))


class SerialException(IOError):
    """Base class for serial port related exceptions."""


class SerialTimeoutException(SerialException):
    """Write timeouts give an exception"""


class PortNotOpenError(SerialException):
    """Port is not open"""

    def __init__(self):
        super(PortNotOpenError, self).__init__(
            "Attempting to use a port that is not open"
        )
