import serial
import serial.tools.list_ports
import platform
import time
import RUStack5


try:
    import bluetooth
except:
    print("Warning: pybluez not found, bluetooth functionality will NOT work. If you want to use it, install pybluez using: pip install pybluez. If you use Windows, you may have to install C++ Visual Studio Build Tools before building pybluez with pip.")

__pdoc__={}
__pdoc__['M5Stack.autoconnect_linux'] = False
__pdoc__['M5Stack.autoconnect_windows'] = False
__pdoc__['M5Stack.autoconnect_mac'] = False
__pdoc__['M5Stack.autoconnect_bluetooth_linux'] = False
__pdoc__['M5Stack.autoconnect_bluetooth_windows'] = False
__pdoc__['M5Stack.autoconnect_bluetooth_windows_named'] = False
__pdoc__['M5Stack.autoconnect_bluetooth_mac'] = False
__pdoc__['M5Stack.findport_bluetooth_linux'] = False
__pdoc__['M5Stack.findport_bluetooth_windows'] = False
__pdoc__['M5Stack.findport_bluetooth_windows_named'] = False
__pdoc__['M5Stack.findport_bluetooth_mac'] = False
__pdoc__['M5Stack.read_word'] = False
__pdoc__['M5Stack.send_raw_wait_n_us_read_multiline'] = False
__pdoc__['M5Stack.connect_linux'] = False
__pdoc__['M5Stack.connect_windows'] = False
__pdoc__['M5Stack.connect_mac'] = False
__pdoc__['M5Stack.data_available'] = False
__pdoc__['M5Stack.send_raw_multiline'] = False
__pdoc__['M5Stack.send_raw_multiline_and_wait'] = False
__pdoc__['M5Stack.send_raw_read_n_words'] = False
__pdoc__['M5Stack.send_raw_read_n_words_2'] = False
__pdoc__['M5Stack.send_raw_wait_for_response'] = False
__pdoc__['M5Stack.send_raw_wait_read'] = False
__pdoc__['M5Stack.send_raw_wait_read_2'] = False
__pdoc__['M5Stack.send_raw'] = False
__pdoc__['M5Stack.read_raw'] = False
__pdoc__['M5Stack.findport'] = False

class M5Stack():

    """
    .. image:: ../../../m5stack_grey_small.png
    """

    def __init__(self):
        self.connected=False
        self.debug=False
        self.slow=False
        self.fake_os=""
        self.ser=serial.Serial()


    def findport(self):
        ports = serial.tools.list_ports.comports()
        portfound=False
        portname=''
        for port, desc, hwid in sorted(ports):
            if 'VID:PID=10C4:EA60' in hwid: # check if serial port uses this UART
                portfound=True
                portname=port
                break
        return(portfound,portname)


    def findport_bluetooth_windows(self):
        stackfound=False
        portfound=False
        stackmac=""
        portname=""

        while stackfound==False:
            print("Discovering devices...")
            devicelist=bluetooth.discover_devices(duration=1,lookup_names=True)
            for mac,name in devicelist:
                if "M5Stack" in name:
                    stackfound=True
                    print("M5Stack found!")
                    stackmac=mac.replace(":","")
                    break
        print("Finding matching COM-port..." )
        comportlist=serial.tools.list_ports.comports()
        for port,name,id in comportlist:
            if (stackmac in id):
                print("COM-port="+port)
                portfound=True
                portname=port
                break

        return(portfound,portname)

    def findport_bluetooth_windows_named(self,namestring):
        stackfound=False
        portfound=False
        stackmac=""
        portname=""

        while stackfound==False:
            print("Discovering devices...")
            devicelist=bluetooth.discover_devices(duration=1,lookup_names=True)
            for mac,name in devicelist:
                if name==namestring:
                    stackfound=True
                    print(namestring+" found!")
                    stackmac=mac.replace(":","")
                    break
        print("Finding matching COM-port..." )
        comportlist=serial.tools.list_ports.comports()
        for port,name,id in comportlist:
            if (stackmac in id):
                print("COM-port="+port)
                portfound=True
                portname=port
                break

        return(portfound,portname)

    def findport_bluetooth_linux(self):
        ports = serial.tools.list_ports.comports()
        portfound=False
        portname=''
        for port, desc, hwid in sorted(ports):
            print(port)
            if 'rfcomm' in port: # check if serial port uses this UART
                testser=serial.Serial()
                testser.port=port
                try:
                    print("testing port:"+port)
                    testser.open()
                    print("port found!")
                    portfound=True
                    portname=port
                    break
                except:
                    pass
        return(portfound,portname)

    def findport_bluetooth_mac(self):
        ports = serial.tools.list_ports.comports()
        portfound=False
        portname=''
        for port, desc, hwid in sorted(ports):
            if 'VID:PID=10C4:EA60' in hwid: # check if serial port uses this UART
                portfound=True
                portname=port
                break
        return(portfound,portname)



    #connect functions:
    def connect(self,port:str)->None:
        """
Establish connection with the M5Stack through a specified serial port. Example:

    mystack.connect("COM1") # windows
    # or
    mystack.connect("/dev/ttyUSB0") # linux
        """
        self.connect_windows(port)

    def connect_windows(self,port):
        self.ser.port=port
        self.ser.timeout=1
        self.ser.baudrate=115200
        self.ser.rts=0
        self.ser.dtr=0
        try:
            self.ser.open()
            self.ser.flush()
            self.connected=True
        except:
            self.connected=False

    def connect_linux(self,port):
        self.ser.port=port
        self.ser.timeout=1
        self.ser.baudrate=115200
        try:
            self.ser.open()
            self.ser.flush()
            self.connected=True
        except:
            self.connected=False

    def connect_mac(self,port):
        self.ser.port=port
        self.ser.timeout=1
        self.ser.baudrate=115200
        try:
            self.ser.open()
            self.ser.flush()
            self.connected=True
        except:
            self.connected=False

    #autoconnect functions:
    def autoconnect_windows(self):
        found,portname=self.findport()
        if found:
            self.ser=serial.Serial()
            self.ser.port=portname
            self.ser.timeout=1
            self.ser.baudrate=115200
            self.ser.rts=0
            self.ser.dtr=0
            try:
                self.ser.open()
                self.connected=True
                if self.debug:
                    print("Connected to M5Stack from a Windows machine on on port:"+portname)

            except:
                self.connected=False
        else:
            self.connected=False

    def autoconnect_linux(self):
        found,portname=self.findport()
        if found:
            self.ser=serial.Serial()
            self.ser.port=portname
            self.ser.timeout=1
            self.ser.baudrate=115200
            try:
                self.ser.open()
                self.connected=True
                if self.debug:
                    print("Connected to M5Stack from a Linux machine on port:"+portname)

            except:
                self.connected=False
        else:
            self.connected=False

    def autoconnect_mac(self):
        found,portname=self.findport()
        if found:
            self.ser=serial.Serial()
            self.ser.port=portname
            self.ser.timeout=1
            self.ser.baudrate=115200
            try:
                self.ser.open()
                self.connected=True
                if self.debug:
                    print("Connected to M5Stack from a Mac on port:"+portname)
            except:
                self.connected=False
        else:
            self.connected=False

    #autoconnect functions:
    def autoconnect_bluetooth_windows(self):
        found,portname=self.findport_bluetooth_windows()
        if found:
            self.ser=serial.Serial()
            self.ser.port=portname
            self.ser.timeout=1
            self.ser.baudrate=115200
            self.ser.rts=0
            self.ser.dtr=0
            try:
                self.ser.open()
                self.connected=True
                if self.debug:
                    print("Connected to M5Stack from a Windows machine on on port:"+portname)

            except:
                self.connected=False
        else:
            self.connected=False

    def autoconnect_bluetooth_windows_named(self,namestring):
        found,portname=self.findport_bluetooth_windows_named(namestring)
        if found:
            self.ser=serial.Serial()
            self.ser.port=portname
            self.ser.timeout=1
            self.ser.baudrate=115200
            self.ser.rts=0
            self.ser.dtr=0
            try:
                self.ser.open()
                self.connected=True
                if self.debug:
                    print("Connected to M5Stack from a Windows machine on on port:"+portname)

            except:
                self.connected=False
        else:
            self.connected=False

    def autoconnect_bluetooth_linux(self):

        found,portname=self.findport_bluetooth_linux()
        if found:
            self.ser=serial.Serial()
            self.ser.port=portname
            self.ser.timeout=1
            self.ser.baudrate=115200
            try:
                self.ser.open()
                self.connected=True
                if self.debug:
                    print("Connected to M5Stack from a Linux machine on port:"+portname)

            except:
                self.connected=False
        else:
            self.connected=False

    def autoconnect_bluetooth_mac(self):
        found,portname=self.findport_bluetooth_mac()
        if found:
            self.ser=serial.Serial()
            self.ser.port=portname
            self.ser.timeout=1
            self.ser.baudrate=115200
            try:
                self.ser.open()
                self.connected=True
                if self.debug:
                    print("Connected to M5Stack from a Mac on port:"+portname)
            except:
                self.connected=False
        else:
            self.connected=False




    def autoconnect_bluetooth(self):
        """
Automatically establish a bluetooth connection with the first paired M5Stack. 

Example:

    mystack=RUStack5.Devices.M5Stack()

    mystack.autoconnect_bluetooth()
        """
        
        connect_table = {'Linux' : self.autoconnect_bluetooth_linux,
                        'Windows' : self.autoconnect_bluetooth_windows,
                        'Darwin' : self.autoconnect_bluetooth_mac}

        # connect to spoofed OS
        if self.fake_os=="Darwin":
            self.autoconnect_bluetooth_mac()
        if self.fake_os=="Linux":
            self.autoconnect_bluetooth_linux()
        if self.fake_os=="Windows":
            self.autoconnect_bluetooth_windows()

        # connect to true OS
        if self.fake_os=="":
            connect_table[platform.system()]()

    def autoconnect_bluetooth_named(self,namestring):


        os=platform.system() # find the os
        if (self.fake_os!=""): # if a fake os is specified change os to its name
            os=self.fake_os

        if os=="Darwin":
            self.autoconnect_bluetooth_mac()
        if os=="Linux":
            self.autoconnect_bluetooth_linux()
        if os=="Windows":
            self.autoconnect_bluetooth_windows_named(namestring)




    def autoconnect(self):
        """
Automatically establish a serial port connection with the first M5Stack found in the system. 

Example:

    mystack=RUStack5.Devices.M5Stack()

    mystack.autoconnect()
        """
        connect_table = {'Linux' : self.autoconnect_linux,
                        'Windows' : self.autoconnect_windows,
                        'Darwin' : self.autoconnect_mac}

        # connect to spoofed OS
        if self.fake_os=="Darwin":
            self.autoconnect_mac()
        if self.fake_os=="Linux":
            self.autoconnect_linux()
        if self.fake_os=="Windows":
            self.autoconnect_windows()

        # connect to true OS
        if self.fake_os=="":
            connect_table[platform.system()]()

    def disconnect(self):
        '''
        Closes the connection with the M5Stack, freeing up the serial port.
        '''
        if self.ser.isOpen():
            self.ser.close()
        self.connected=False

    def send_raw(self,s):
        if (self.connected):
            self.ser.write(s)
            if self.debug:
                print("Sent:")
                print(s)
            response=self.ser.readline()
            if self.debug:
                print ("Received:")
                print (response)
            if self.slow:
                time.sleep(0.3)
            return response
        else:
            return(None)

    def send_raw_wait_for_response(self,s):
        if (self.connected):
            self.ser.write(s)
            if self.debug:
                print("Sent:")
                print(s)
            while not self.data_available():
                pass
            response=self.ser.readline()
            if self.debug:
                print ("Received:")
                print (response)
            if self.slow:
                time.sleep(0.3)
            return response
        else:
            return(None)


    def read_raw(self):
        if (self.connected):
            response=self.ser.readline()
            if self.debug:
                print ("Received:")
                print (response)
            if self.slow:
                time.sleep(0.3)
            return response
        else:
            return(None)

    def send_raw_read_n_words(self,s,n):
        if (self.connected):
            self.ser.write(s)
            if self.debug:
                print("Sent:")
                print(s)
            while not self.data_available():
                pass
            resultlist=[]
            for i in range(0,n):
                msb=self.ser.read(1)[0]&0x0F
                lsb=self.ser.read(1)[0]

                resultlist.append(msb*256+lsb)
            self.ser.reset_input_buffer()
            return resultlist
        else:
            return(None)

    def send_raw_read_n_words_2(self,s,n):
        if (self.connected):
            self.ser.write(s)
            if self.debug:
                print("Sent:")
                print(s)
            while not self.data_available():
                pass
            resultlist=[]
            for i in range(0,n):
                msb=self.ser.read(1)[0]
                lsb=self.ser.read(1)[0]
                resultlist.append(msb*256+lsb)
            self.ser.reset_input_buffer()
            return resultlist
        else:
            return(None)

    def read_word(self):
        if (self.connected):

            while not self.data_available(): # wait for a byte to become available
                pass
            msb=self.ser.read(1)[0] # read it

            while not self.data_available(): # next byte
                pass
            lsb=self.ser.read(1)[0]

            result=msb*256+lsb
            return result
        else:
            return(None)


    def send_raw_wait_read(self,s):
        if (self.connected):
            self.ser.reset_input_buffer()
            self.ser.write(s)
            if self.debug:
                print("Sent:")
                print(s)
            while not self.data_available():
                pass
            self.ser.reset_input_buffer()
            return(None)
        else:
            return(None)

    def send_raw_wait_read_2(self,s):
        if (self.connected):
            self.ser.reset_input_buffer()
            self.ser.write(s)
            if self.debug:
                print("Sent:")
                print(s)
            while not self.data_available():
                pass
            number_of_samples=Response_to_int(self.ser.readline())
            self.ser.reset_input_buffer()
            return(number_of_samples)
        else:
            return(None)


    def send_raw_multiline(self,s):
        if (self.connected):
            self.ser.write(s)
            if self.debug:
                print("Sent:")
                print(s)
            response=self.ser.readlines()
            if self.debug:
                print ("Received:")
                print (response)
            if self.slow:
                time.sleep(0.3)
            return response
        else:
            return(None)

    def send_raw_multiline_and_wait(self,s,waittime):
        if (self.connected):
            self.ser.readlines()
            self.ser.write(s)

            if self.debug:
                print("Sent:")
                print(s)
            print("waiting....")
            time.sleep((waittime/1000)+2)
            response=self.ser.readlines()
            if self.debug:
                print ("Received:")
                print (response)
            if self.slow:
                time.sleep(0.3)

            return response
        else:
            return(None)

    def send_raw_wait_n_us_read_multiline(self,s,waittime):
        if (self.connected):
            self.ser.readlines()
            self.ser.write(s)

            if self.debug:
                print("Sent:")
                print(s)
            print("waiting....")
            time.sleep(waittime/1000000)
            time.sleep(0.001) # wait a little bit longer to ensure measurement is really finished
            response=self.ser.readlines()
            if self.debug:
                print ("Received:")
                print (response)
            if self.slow:
                time.sleep(0.3)

            return response
        else:
            return(None)

    def data_available(self):
        return self.ser.in_waiting



