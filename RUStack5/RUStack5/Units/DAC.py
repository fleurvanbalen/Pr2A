import RUStack5
import time
from RUStack5.Tools import *
__pdoc__={}
__pdoc__['DAC.selftest']=False
__pdoc__['DAC.millivolt']=False
__pdoc__['DAC.value']=False
__pdoc__['DAC.millivolt']=False


class DAC:
    '''
    Support for the M5Stack Digital to Analog converter (DAC) unit.
    '''
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._millivolt=0
        self._value=0

    def set_millivolt(self,v):
        '''
        Set the voltage at the output of the DAC to the specified value (in mV)
        '''
        sendstring=">DAC.SetVoltage("+str(v)+")"
        self.stack.send_raw(sendstring.encode('utf-8'))


    def set_value(self,v):
        '''
        Set the voltage at the output of the DAC to the specified value in units of 1/2048 of the full output voltage (3.3V).
        '''
        sendstring=">DAC.SetValue("+str(v)+")"
        self.stack.send_raw(sendstring.encode('utf-8'))

    def init(self):
        """
        Initialize the DAC unit.
        """
        if (self.stack.connected):
            self.stack.send_raw(b">DAC.initialize()")

    def selftest(self):
        print("setting dac to 0.5V")
        self.millivolt=500
        time.sleep(1)
        print("setting dac to 1V")
        self.millivolt=1000
        time.sleep(1)
        print("setting dac to 2V")
        self.millivolt=2000
        time.sleep(1)
        print("setting dac to 0V through value")
        self.value=0
        time.sleep(1)



    @property
    def millivolt(self):
        return self._millivolt
    @millivolt.setter
    def millivolt(self, value):
        self.set_millivolt(value)

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self.set_value(value)






