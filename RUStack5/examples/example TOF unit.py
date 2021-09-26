import RUStack5 # import the library
mystack=RUStack5.Devices.M5Stack() # create the device object
tof=RUStack5.Units.TOF(mystack)
mystack.autoconnect() # connect to the device
tof.init()
print(tof.get_distance()) # print the distance as measured by the TOF unit
mystack.disconnect()