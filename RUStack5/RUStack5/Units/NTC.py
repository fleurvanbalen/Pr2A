import RUStack5
from RUStack5.Tools import *
__pdoc__={}
__pdoc__['NTC.selftest']=False
__pdoc__['NTC.read_temp']=False

class NTC():
    def __init__(self,RUStack_parent):
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
        self.rate=4
        self.gain=8
        self._voltage=0
        self._temperature=0

    def init(self):
        self.stack.send_raw(b">ADC.Initialize()")

    def set_gain(self,r):
        for (range, sendstring) in self.GAIN_TABLE:
            if range==r:
                self.stack.send_raw(sendstring)
                self.gain=r
                break

    def set_rate(self,r):
        for (range, sendstring) in self.RATE_TABLE:
            if range==r:
                self.stack.send_raw(sendstring)
                self.rate=r
                break

    def read_ADC(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">ADC.GetValue()")
            return Response_to_float(response)
        else:
            return(None)

    def read_temp(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">ADC.GetNTCTemp()")
            return Response_to_float(response)
        else:
            return(None)

    def selftest(self):
        print("NTC:")
        print(self.temperature)

    @property
    def adc_value(self):
        return self.read_ADC()
    @property
    def voltage(self):
        return self.adc_value/32768*self.rate/8*3.3*4/self.gain
    @property
    def temperature(self):
        return self.read_temp()
