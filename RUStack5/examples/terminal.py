import RUStack5
import tkinter
import time

history=[
        ">M5Accelerometer.GetValue(x)",
        ">M5Test.ScanI2C()",
        ">M5Power.GetBatteryLevel()",
        ">M5Test.LastError()",
        ">M5Speaker.beep()"]

items_back=0

def Poll():
    read_char=""
    if mystack.ser.isOpen:
        while (mystack.ser.inWaiting()>0):
            if (mystack.ser.inWaiting() > 0):
                read_char=read_char+chr(mystack.ser.read(size=1)[0])
            time.sleep(0.001)
        if read_char!=[]:
            ReceivedField.insert(tkinter.INSERT,read_char)
    top.after(1,Poll)

def SendInput():
    command=InputString.get()
    mystack.ser.write(command.encode('utf-8'))
    history.append(command)

def OnEnter(event):
    global items_back
    SendInput()
    InputString.set(">")
    items_back=0

def OnUp(event):
    global items_back
    if items_back<len(history):
        items_back=items_back+1
    InputString.set(history[len(history)-items_back])
    InputField.icursor(len(InputString.get()))

def OnDown(event):
    global items_back
    if items_back>1:
        items_back=items_back-1
    InputString.set(history[len(history)-items_back])
    InputField.icursor(len(InputString.get()))

top=tkinter.Tk()
top.title("RUStack test terminal")
MaxWidth=top.winfo_screenwidth()
MaxHeight=top.winfo_screenheight()
top.minsize(50, 50)
top.maxsize(MaxWidth, MaxHeight)
InputString=tkinter.StringVar()
InputString.set(">")

InputField=tkinter.Entry(top,textvariable=InputString)
InputField.grid(row=1, column=0, sticky="nsew")
InputField.bind("<Return>",OnEnter)
InputField.bind("<Up>",OnUp)
InputField.bind("<Down>",OnDown)

ReceivedField=tkinter.Text(top,bg='white')
ReceivedField.grid(row=2,column=0,  sticky="nsew")

mystack=RUStack5.Devices.M5Stack()
print("connecting...")
mystack.autoconnect()

InputField.focus()
InputField.icursor(len(InputString.get()))

top.after(1,Poll)
top.mainloop()
mystack.disconnect()
print("disconnected...")