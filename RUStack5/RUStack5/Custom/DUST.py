import RUStack5
from RUStack5.Tools import *

'''
Support for the SDS011 precision dust sensor.
'''

class DUST():
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._pm2_5=0
        self._pm10=0

    def wakeup(self):
        '''
        Starts the fan and laser inside the sensor, preparing it for data acquisition.
        '''

        if (self.stack.connected):
            response=self.stack.send_raw(b">SDS011.WakeUp()")
            return Response_to_float(response)
        else:
            return(None)

    def pms_split(self,s):
        a=-1
        b=-1
        try:
            a,b=s.split(",")
        except:
            pass
        return(a,b)


    def read_pms(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">SDS011.read()")
            rsp_string=Response_to_string(response)
            a,b=self.pms_split(rsp_string)
            return float(a),float(b)
        else:
            return None,None

    def sleep(self):
        '''
        Puts the sensor into sleep mode, saving current and life expectancy of the laser and fan.
        '''
        if (self.stack.connected):
            response=self.stack.send_raw(b">SDS011.sleep()")
            return Response_to_float(response)
        else:
            return(None)

    def init(self):
        '''
        Sets up communication and starts the laser and fan of the sensor.
        '''
        if (self.stack.connected):
            response=self.stack.send_raw(b">SDS011.Initialize()")
            return Response_to_float(response)
        else:
            return(None)


    def selftest(self):
        self.init()
        self.start()
        time.sleep(3)
        print(self.pms)
        print(self.pm2_5)
        print(self.pm10)
        self.sleep()

    @property
    def pm2_5(self):
        '''
        Returns the concentration of PM2.5 particles in the air sampled by the sensor.
        '''
        r2_5,r10=self.read_pms()
        return(r2_5)

    @property
    def pm10(self):
        '''
        Returns the concentration of PM10 particles in the air sampled by the sensor.
        '''

        r2_5,r10=self.read_pms()
        return(r10)

    @property
    def pms(self):
        '''
        Returns a tuple with both PM2.5 and PM10 particle concentration: (PM2.5,PM10)
        '''

        return self.read_pms()
