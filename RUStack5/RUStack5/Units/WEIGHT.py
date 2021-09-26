import RUStack5
from RUStack5.Tools import *
__pdoc__={}
__pdoc__['WEIGHT.selftest']=False


class WEIGHT():
    """
    Class for acquiring data from the M5Stack HX711 force sensor unit.
    """

    def __init__(self,RUStack_parent:RUStack5.Devices.M5Stack):
        self.stack=RUStack_parent
        self._weight=0
        self._scalefactor=0
        self.GAIN_TABLE = (
            (32.0,b">WEIGHT.Configure(GAIN=32)"),
            (64.0,b">WEIGHT.Configure(GAIN=64)"),
            (128.0,b">WEIGHT.Configure(GAIN=128)")
            )


    def _getgram(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw(b">WEIGHT.GetValue(force)"))
        else:
            return(-99999)


    def selftest(self):
        '''
        Perform a selftest comprising:\n
        - Print the current value of weight.\n
        '''
        print("sending init command:")
        self.init()
        print("sending reset command:")
        self.reset()

        print("Setting scale factor to 1.23:")
        self.set_scalefactor(1.23)
        print("Reading back scale factor:")
        print(self.scalefactor)

        print("Setting scale factor to 1, getting weight:")
        self.set_scalefactor(1)
        print(self.weight)

        print("Setting scale factor to 2, getting weight:")
        self.set_scalefactor(2)
        print(self.weight)

        print("setting scalefactor back to 1:")
        self.set_scalefactor(1)

#        value of 32 currently unsupported
#        print("Setting gain to 32, getting weight:")
#        self.set_gain(32)
#        print(self.weight)

        print("Setting gain to 64, getting weight:")
        self.set_gain(64)
        print(self.weight)

        print("Setting gain to 128, getting weight:")
        self.set_gain(128)
        print(self.weight)





    def tare(self):
        '''
        Reset the WEIGHT force sensor.
        '''
        if (self.stack.connected):
            self.stack.send_raw(b">WEIGHT.Tare()")

    def init(self):
        '''
        Initialize the WEIGHT force sensor.
        '''
        if (self.stack.connected):
            self.stack.send_raw(b">WEIGHT.initialize()")

    def set_gain(self,g):
        '''
        Set the gain of the sensor. Valid values are 32, 64 and 128. The value of 32 might not be supported yet due to an error in the Arduino HX711 library.
        '''
        for (r, sendstring) in self.GAIN_TABLE:
            if float(r)==float(g):
                self.stack.send_raw(sendstring)
                self._gain=r
                break

    def set_scalefactor(self,s):
        '''
        Set the scalefactor of the device.
        '''
        sendstring=">WEIGHT.Configure(ScaleFactor="+str(s)+")"
        self.stack.send_raw(sendstring.encode('utf-8'))

    def _get_scalefactor(self):
        '''
        Get the current scalefactor of the device.
        '''
        if (self.stack.connected):
            response=self.stack.send_raw(b">WEIGHT.GetValue(ScaleFactor)")
            return Response_to_float(response)
        else:
            return(None)


    @property
    def weight(self):
        '''
        Returns an uncalibrated value proportional to the force currently acting upon the force sensor.
        '''
        return self._getgram()

    @property
    def scalefactor(self):
        '''
        Returns the current scale factor.
        '''
        return self._get_scalefactor()




