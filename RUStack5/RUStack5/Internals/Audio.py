# Audio
from RUStack5.Tools import *
__pdoc__={}
__pdoc__['Audio.selftest'] = False
class Audio():
    '''
    Support for the M5Stack's internal speaker.
    '''
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
    def beep(self):
        '''
        Generate a short beep.
        '''
        if (self.stack.connected):
            self.stack.ser.write(b">M5Speaker.Beep()")
            response=self.stack.ser.readline()
 #   def beep(self):
 #       self.stack.send_raw(b">Audio.beep()")
    def selftest(self):
        self.beep()