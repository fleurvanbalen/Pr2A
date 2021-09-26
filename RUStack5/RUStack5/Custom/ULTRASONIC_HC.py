import RUStack5
from RUStack5.Tools import *

class ULTRASONIC_HC():
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._hittime=0
        self._distance=0
        self._timeout=0

    def read_roundtriptime(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">HCSR04.GetValue(RoundTripTime)")
            return Response_to_float(response)
        else:
            return(None)

    def read_distance(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">HCSR04.GetValue(distance)")
            return Response_to_float(response)
        else:
            return(None)

    def read_timeout(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">HCSR04.GetValue(timeout)")
            return Response_to_float(response)
        else:
            return(None)

    def set_timeout(self,timeout):
        if (self.stack.connected):
            sendstring=">HCSR04.Configure(timeout="+str(timeout)+")"
            self.stack.send_raw(sendstring.encode('UTF-8'))


    def init(self):
        if (self.stack.connected):
            self.stack.send_raw(b">HCSR04.Initialize()")

    def selftest(self):
        print(self.hittime)
        print(self.distance)
        print(self.timeout)

    @property
    def roundtriptime(self):
        return self.read_roundtriptime()
    @property
    def distance(self):
        return self.read_distance()
    @property
    def timeout(self):
        return self.read_timeout()
