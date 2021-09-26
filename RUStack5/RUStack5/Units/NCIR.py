import RUStack5
from RUStack5.Tools import *

__pdoc__={}
__pdoc__['NCIR.selftest']=False
__pdoc__['NCIR.read_temp']=False

class NCIR():
    '''
    Support for M5Stack's NCIR unit.
    '''

    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._temperature=0

    def read_temp(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw(b">NCIR.GetTemperature()"))
        else:
            return(-99999)

    def selftest(self):
        print(self.temperature)

    def init(self):
        '''
        Initialize the sensor.
        '''
        if (self.stack.connected):
            self.stack.send_raw(b">NCIR.initialize()")

    @property
    def temperature(self):
        '''
        Returns the temperature as measured by the sensor.
        '''

        return self.read_temp()
