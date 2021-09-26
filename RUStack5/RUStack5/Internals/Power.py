import RUStack5
from RUStack5.Tools import *

__pdoc__={}
__pdoc__['Power.selftest'] = False
__pdoc__['Power.read_charging'] = False
__pdoc__['Power.read_level'] = False

class Power:
    """
    Support for the M5Stack's power management and charge controller.
    """
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._battery_level=0
        self._charging=False

    def read_level(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw(b">M5Power.GetBatteryLevel()"))
        else:
            return(-99999)

    def read_charging(self):
        if (self.stack.connected):
            state = Response_to_string(self.stack.send_raw(b">M5Power.GetChargingStatus()"))
            print(state)
            if state=="Charging\r\n":
                return True
            else:
                return False

    def selftest(self):
        print(self.battery_level)
        print(self.charging)

    @property
    def battery_level(self):
        '''
        Returns the battery level in %
        '''
        return self.read_level()
    @property
    def charging(self)->bool:
        '''
        Returns the charging state.
        '''
        return self.read_charging()
