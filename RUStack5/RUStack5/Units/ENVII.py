import RUStack5
from RUStack5.Tools import *

__pdoc__={}
__pdoc__['ENVII.selftest']=False
__pdoc__['ENVII.read_hum']=False
__pdoc__['ENVII.read_press']=False
__pdoc__['ENVII.read_temp']=False

class ENVII():
    '''
    Support for M5Stack's ENVII unit.
    '''

    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._temperature=0
        self._humidity=0
        self._pressure=0

    def read_temp(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw(b">ENVII.GetTemperature()"))
        else:
            return(-99999)

    def read_hum(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw(b">ENVII.GetHumidity()"))
        else:
            return(-99999)

    def read_press(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw(b">ENVII.GetPressure()"))
        else:
            return(-99999)

    def selftest(self):
        print("ENVII tem,hum,press:")
        print(self.temperature)
        print(self.humidity)
        print(self.pressure)

    def init(self):
        '''
        Initialize the sensor.
        '''
        if (self.stack.connected):
            self.stack.send_raw(b">ENVII.Initialize()")



    @property
    def temperature(self):
        '''
        Returns the temperature as measured by the sensor.
        '''

        return self.read_temp()
    @property
    def humidity(self):
        '''
        Returns the hummidity as measured by the sensor.
        '''

        return self.read_hum()
    @property
    def pressure(self):
        '''
        Returns the pressure as measured by the sensor. Use the init-method to initialize the sensor before use.
        '''

        return self.read_press()