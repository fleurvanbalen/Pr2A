"""
.. image:: ../../Media/stack_and_units_small.png
.. include:: ./documentation.md
"""

# functions hidden from docs:
__pdoc__ = {}
__pdoc__['RUStack.Chips'] = False
__pdoc__['RUStack.Tools'] = False
__pdoc__['RUStack.Internals.Test']=False
__pdoc__['RUStack.Internals.ESP32_hall']=False
#__pdoc__['RUStack.Devices.M5Stack.autoconnect_mac'] = "test"

#__pdoc__['RUStack.Devices.M5Stack.autoconnect_mac()'] = False






import serial
import serial.tools.list_ports
import platform
import time
import RUStack5.Devices
import RUStack5.Internals
import RUStack5.Units
import RUStack5.Modules
import RUStack5.Custom
import RUStack5.Tools
import RUStack5.Hubs



