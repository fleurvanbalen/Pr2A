import time
from RUStack5.Tools import *

class StepMotor:
    """
    Interface class to control the M5Stack servo module.
    .. image:: ../../../servo_small.png
    """
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent


    def send_command(self,s):
        '''
        Send a gcode command.
        '''
        if (self.stack.connected):
            sendstring=">StepMotor.G-code("+s+")"
            self.stack.send_raw(sendstring.encode('utf-8'))
            return(None)
        else:
            return(None)
