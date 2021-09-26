import RUStack5
from RUStack5.Tools.Conversion import *
__pdoc__={}
__pdoc__['LASER_RX.selftest']=False
class LASER_RX():
    """
    Support for the LASER_RX unit.
    """
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self.mi=5000000

    def init(self):
        '''
        Initializes the sensor.
        '''
        if (self.stack.connected):
            sendstring=">LaserRX.Initialize()"
            response=self.stack.send_raw_multiline(sendstring.encode('utf-8'))
            self.mi=5000000
            return response
        else:
            return(None)

    def configure(self,port,interval,measurement_type):
        '''

        '''
        if (self.stack.connected):
            sendstring=">LaserRX.Configure(port="+str(port)+",MeasuringInterval="+str(interval)+",MeasurementType="+str(measurement_type)+")"
            self.mi=interval

        else:
            return(None)


    def get_interval_list(self):
        '''

        '''
        if (self.stack.connected):
            sendstring=">LaserRX.GetTriggerEventInterval()"
            response=send_raw_wait_n_us_read_multiline(sendstring,self.mi)
            values=[]
            for l in response:
                values.append(float(l))
            return values
        else:
            return(None)

