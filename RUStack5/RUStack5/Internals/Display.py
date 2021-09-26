# Display
import time
from RUStack5.Tools import *
__pdoc__={}
__pdoc__['Display.selftest'] = False

class Display():
    """ Support for the M5Stack's display functions. """

    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
    def turn_on(self):
        """Turns the display on."""
        self.stack.send_raw(b">M5Display.TurnOn()")
    def turn_off(self):
        """Turns the display off."""
        self.stack.send_raw(b">M5Display.TurnOff()")
    def selftest(self):
        """Performs a self test comprising: \n
        -Turn off the display for 1 second \n
        -Turn on the display for 1 second \n
        -Turn off the display for 1 second \n
        -Turn the display back on
        """
        print("display on/off")
        self.turn_off()
        time.sleep(1)
        self.turn_on()
        time.sleep(1)
        self.turn_off()
        time.sleep(1)
        self.turn_on()
