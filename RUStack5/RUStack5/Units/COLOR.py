import RUStack5
from RUStack5.Tools import *
import time
__pdoc__={}
__pdoc__['COLOR.selftest']=False

class COLOR():
    '''
    Support for the M5Stack COLOR Unit.
    '''
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._red=0
        self._green=0
        self._blue=0
        self._clear=0
        self._all=0,0,0,0
        self.GAIN_TABLE = (
            (1.0,b">Color.Configure(GAIN=1)"),
            (4.0,b">Color.Configure(GAIN=4)"),
            (16.0,b">Color.Configure(GAIN=16)"),
            (60.0,b">Color.Configure(GAIN=60)"))
        self.INT_TIME_TABLE = (
            (2.4,b">Color.Configure(integrationTime=2)"),
            (24.0,b">Color.Configure(integrationTime=24)"),
            (50.0,b">Color.Configure(integrationTime=50)"),
            (101.0,b">Color.Configure(integrationTime=101)"),
            (154.0,b">Color.Configure(integrationTime=154)"),
            (700.0,b">Color.Configure(integrationTime=700)"))

        self._gain=4.0
        self._int_time=50.0

    def _read_red(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw_wait_for_response(b">Color.GetValue(red)"))
        else:
            return(-99999)

    def _read_green(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw_wait_for_response(b">Color.GetValue(green)"))
        else:
            return(-99999)

    def _read_blue(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw_wait_for_response(b">Color.GetValue(blue)"))
        else:
            return(-99999)

    def _read_clear(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw_wait_for_response(b">Color.GetValue(clear)"))
        else:
            return(-99999)

    def _read_all(self)->list:
        if (self.stack.connected):
            return Response_to_four_floats(self.stack.send_raw_wait_for_response(b">Color.GetValues()"))
        else:
            return(-99999)


    def selftest(self):
        print("CRGB acquired separately:")
        print(self.clear)
        print(self.red)
        print(self.green)
        print(self.blue)
        print("Acquired simultaneously:")
        print(self.all)
        print("Setting gains:")
        self.gain=1
        time.sleep(0.2)
        self.gain=4
        time.sleep(0.2)
        self.gain=16
        time.sleep(0.2)
        self.gain=60
        time.sleep(0.2)
        self.int_time=2.4
        time.sleep(0.2)
        self.int_time=24
        time.sleep(0.2)
        self.int_time=50
        time.sleep(0.2)
        self.int_time=101
        time.sleep(0.2)
        self.int_time=154
        time.sleep(0.2)
        self.int_time=700

    def set_gain(self,g):
        '''
        Set the gain of the sensor's pre-amplifier. Valid values are 1, 4, 16, 60.
        '''
        for (r, sendstring) in self.GAIN_TABLE:
            if float(r)==float(g):
                self.stack.send_raw(sendstring)
                self._gain=r
                break

    def set_int_time(self,i):
        '''
        Set the sensor's integration time. Valid values are: 2.4, 24, 50, 101, 154, 700.
        '''
        for (r, sendstring) in self.INT_TIME_TABLE:
            if float(r)==float(i):
                self.stack.send_raw(sendstring)
                self._int_time=r
                break


    def init(self):
        '''
        Initialize the sensor.
        '''
        if (self.stack.connected):
            self.stack.send_raw(b">Color.Initialize()")

    @property
    def red(self):
        '''
        Returns the intensity of the red component of the light striking the sensor.
        '''
        return self._read_red()
    @property
    def green(self):
        '''
        Returns the intensity of the red component of the light striking the sensor.
        '''
        return self._read_green()
    @property
    def blue(self):
        '''
        Returns the intensity of the red component of the light striking the sensor.
        '''
        return self._read_blue()
    @property
    def clear(self):
        '''
        Returns the intensity of the unfiltered light striking the sensor.
        '''
        return self._read_clear()
    @property
    def all(self)->list:
        '''
        Measure all four light intensities at once. Returns a list of four values as [clear,red,green,blue]
        '''
        return self._read_all()
