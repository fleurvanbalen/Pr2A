import RUStack5 # import the M5Stack library
import time # import date and time functions to allow timestamp generation

mystack=RUStack5.Devices.M5Stack() # create the device object
display=RUStack5.Internals.Display(mystack) # create the object associated with the display
acc=RUStack5.Internals.IMU(mystack) # create the object associated with the accelerometer

mystack.autoconnect() # connect through a serial port connection
display.turn_off() # turn off the display


file = open("datalog.txt","w") # open a file with write permission

starttime=time.time_ns()//1000 # store initial value of time since epoch (in nanoseconds). Divide by 1000 to convert to microseconds. This initial time value will be subtracted from later time measurements to get relative time since program start.

print("Logging data to file...")
try:
    while True:
        file.write(str(time.time_ns()//1000-starttime)) # write a timestamp
        file.write(",") # followed by a semicolon
        file.write(str(acc.accX)) # and the value measured by the internal accelerometer
        file.write("\n") # and a new line

except KeyboardInterrupt: # stop on a keypress. Note: in Pyzo no interrupt is generated when a key is pressed. Instead, use the yellow lighting bolt in the console window's button bar to generate a keyboard interrupt in Pyzo.
    pass

display.turn_on() # Turn the M5Stack's display back on
mystack.disconnect() # disconnect
file.close() # and close the file.
print("Logging finished, file closed.")