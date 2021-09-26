import RUStack5 # import the library

mystack=RUStack5.Devices.M5Stack() # create the device object
color=RUStack5.Units.COLOR(mystack)
mystack.autoconnect() # connect to the device

color.init()

color.set_gain(4) # amplifier gain [1|4|16|60]
color.set_int_time(154) # integration time [2.4|24|50|101|154|700]

print('Red component:')
print(color.red)
print('')

print('Green component:')
print(color.green)
print('')

print('Blue component:')
print(color.blue)
print('')

print('Clear component:')
print(color.clear)
print('')

print('Ĺist of C,R,G,B values:')
print(color.all)


mystack.disconnect()