import time
from RUStack5.Tools import *

class SERVO:
    """
    Interface class to control the M5Stack servo module.
    .. image:: ../../../servo_small.png
    """
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent

    def init(self):
        '''
        Initialize the servo module.
        '''
        sendstring=">Servo.Initialize()"
        self.stack.send_raw(sendstring.encode('utf-8'))

    def set_angle(self,port:int,angle:int):
        '''
        Set the servo connected to the specified port to the specified angle.
        Valid arguments:
        port=[0..11]
        angle=[0..180]
        '''
        if (self.stack.connected):
            sendstring=">servo.setangle(port="+str(port)+",angle="+str(angle)+")"
            self.stack.send_raw(sendstring.encode('utf-8'))
            return(None)
        else:
            return(None)

    def selftest(self):
        '''
        Performs a selftest comprising:\n
        - Set servo angles on all ports to 0 degrees\n
        - Wait 1 second\n
        - Set servo angles on all ports to 180 degrees\n
        - Wait 1 second\n
        '''
        self.init()
        print("Setting all servo's to 0 degrees")
        for i in (0,1,2,3,4,5,6,7,8,9,10,11):
            self.set_angle(i,0)
        time.sleep(1)
        print("Setting all servo's to 180 degrees")
        for i in (0,1,2,3,4,5,6,7,8,9,10,11):
            self.set_angle(i,180)
        time.sleep(1)


