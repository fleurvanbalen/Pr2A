import RUStack5
mystack=RUStack5.Devices.M5Stack()
acc=RUStack5.Internals.IMU(mystack)

mystack.autoconnect()

print("X,Y,Z")

try:
    while True:
        print(str(acc.accX)+
        ","+
        str(acc.accY)+
        ","+
        str(acc.accZ))

except KeyboardInterrupt:
    pass

mystack.disconnect()
