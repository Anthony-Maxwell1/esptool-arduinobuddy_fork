from java import jclass
from com.chaquo.python import Python

SerialBridgeJava = jclass("org.thatdev.arduinobuddy.SerialBridge")
context = Python.getPlatform().getApplication()

class SerialBridge:
    def __init__(self):
        self.bridge = SerialBridgeJava(context)

    def open(self, device, baudrate=115200):
        self.bridge.open(device, baudrate)

    def close(self):
        self.bridge.close()

    def read(self, size=1):
        return bytes(self.bridge.read(size))

    def write(self, context, data):
        self.bridge.write(data)

    def in_waiting(self):
        return self.bridge.inWaiting()

    def clearInputBuffer(self):
        self.bridge.clearInputBuffer()

    def clearOutputBuffer(self):
        self.bridge.clearOutputBuffer()

def getPorts():
    return list(SerialBridgeJava.getPorts(context))

serial = SerialBridge()
