import RUStack5
from RUStack5.Tools import *

__pdoc__={}
__pdoc__['ADC.selftest']=False

class ADC():
    '''
    Support for the M5Stack ADC unit.
    '''
    def __init__(self,RUStack_parent:RUStack5.Devices.M5Stack):
        self.stack=RUStack_parent
        self._adc_value=0
        self.GAIN_TABLE = (
            (1,b">ADC.Configure(GAIN=1)"),
            (2,b">ADC.Configure(GAIN=2)"),
            (4,b">ADC.Configure(GAIN=4)"),
            (8,b">ADC.Configure(GAIN=8)"))
        self.RATE_TABLE = (
            (8,b">ADC.Configure(SamplingRATE=8)"),
            (16,b">ADC.Configure(SamplingRATE=16)"),
            (32,b">ADC.Configure(SamplingRATE=32)"),
            (128,b">ADC.Configure(SamplingRATE=128)"))
        self.rate=1
        self.gain=8
        self._voltage=0

    def init(self):
        '''
        Initialize the ADC.
        '''
        self.stack.send_raw(b">ADC.Initialize()")

    def set_gain(self,r):
        '''
        Set the gain factor of the ADC pre-amplifier.\n
        Possible values: 1,2,4,8 \n
        '''
        for (range, sendstring) in self.GAIN_TABLE:
            if range==r:
                self.stack.send_raw(sendstring)
                self.gain=r
                break

    def set_rate(self,r):
        '''
        Set the ADC sampling rate.\n
        Possible values: 8,16,32,128\n
        '''
        for (range, sendstring) in self.RATE_TABLE:
            if range==r:
                self.stack.send_raw(sendstring)
                self.rate=r
                break

    def _read_ADC(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">ADC.GetValue()")
            return Response_to_float(response)
        else:
            return(None)

    def selftest(self):
        '''
        Perform a self test comprising:\n
        - Print voltages measured for all combinations of gain and sample rate.
        '''
        for g in (1,2,4,8):
            print("Voltages measured at gain="+str(g)+":")
            self.set_rate(8)
            print("Rate set to 8")
            self.set_gain(g)
            a=self.voltage
            self.set_rate(16)
            print("Rate set to 16")
            self.set_gain(g)
            b=self.voltage
            self.set_rate(32)
            print("Rate set to 32")
            self.set_gain(g)
            c=self.voltage
            self.set_rate(128)
            print("Rate set to 128")
            self.set_gain(g)
            d=self.voltage
            print (a,b,c,d)


    @property
    def adc_value(self):
        """ Returns the voltage measured by the ADC as a value 0-32768"""
        return self._read_ADC()
    @property
    def voltage(self):
        """ Returns the voltage measured by the ADC as a value in Volts. Gain settings are already accounted for in the result."""
        return self.adc_value/32768*self.rate/8*3.3*4/self.gain
