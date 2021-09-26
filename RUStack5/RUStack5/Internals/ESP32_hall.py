# Hall sensor

from RUStack5.Tools import *


class Esp32_hall:
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._value=0

    def read_esp32_hall(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">ESP32_Hall.read()")
            return Response_to_float(response)
        else:
            return(None)

    def set_offset(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">ESP32_Hall.set_offset()")
            return Response_to_float(response)
        else:
            return(None)

    def selftest(self):
        print("Hall test:")
        print(self.value)

    @property
    def value(self):
        return self.read_esp32_hall()
