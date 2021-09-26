from RUStack5.Tools import *

class Test:
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._ms=0
        self._device_list=[]
        self._last_error=""


    def read_last_error(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">M5Test.lasterror()")
            return Response_to_string(response)
        else:
            return(None)

    def clear_last_error(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">M5Test.lasterror(clear)")

    def scan_i2c(self):
        if (self.stack.connected):
            response=self.stack.send_raw_wait_for_response(b">M5Test.ScanI2C()")
            return response.decode(encoding='UTF-8')
        else:
            return(None)





