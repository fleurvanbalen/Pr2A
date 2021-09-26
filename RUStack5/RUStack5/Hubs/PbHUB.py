import RUStack5
__pdoc__={}
__pdoc__['PbHUB.selftest']=False
__pdoc__['PbHUB.datalinestring']=False

class PbHUB():
    '''
    Support for the PbHUB unit. On this hub, there are 6 available channels (0..5) of which both datalines can be controlled to read or write analog or digital data.
    '''
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent

    def datalinestring(self,d):
        if d==0:
            dataline="A"
        if d==1:
            dataline="B"
        if d=="A":
            dataline="A"
        if d=="B":
            dataline="B"
        return(dataline)

    def init(self):
        '''
        Initializes the hub.
        '''
        sendstring=">PbHUB.initialize()"
        self.stack.send_raw(sendstring.encode('utf-8'))

    def analog_read(self,port:int):
        '''
        Returns a value 0-1024 corresponding to the voltage 0-3.3V on dataline A of the specified port.
        '''
        if (self.stack.connected):
            sendstring=">PbHUB.AnalogRead(port="+str(port)+")"
            response=self.stack.send_raw(sendstring.encode('utf-8'))
            return(Response_to_int(response))
        else:
            return(None)

    def digital_read(self,port,dl):
        '''
        Returns a value 0 or 1 depending on the logical state (LOW/HIGH) of the specified dataline (A or B) on the specified port.
        '''

        if (self.stack.connected):
            sendstring=">PbHUB.DigitalRead(port="+str(port)+",DataLine="+self.datalinestring(dl)+")"
            response=self.stack.send_raw(sendstring.encode('utf-8'))
            return(RUStack5.Tools.Response_to_int(response))
        else:
            return(None)

    def analog_write(self,port,dataline,v):
        '''
        Set the voltage on the specified dataline (A or B) of the specified port. Values 0-255 correspond to a voltage of 0-3.3V.
        '''
        if (self.stack.connected):
            sendstring=">PbHUB.AnalogWrite(port="+str(port)+",DataLine="+str(dataline)+",value="+str(v)+")"
            self.stack.send_raw(sendstring.encode('utf-8'))
            return(None)
        else:
            return(None)

    def digital_write(self,port,dataline,v):
        '''
        Set the logical state of the specified dataline (A or B) on the specified port. 0=LOW, 1=HIGH.
        '''

        if (self.stack.connected):
            sendstring=">PbHUB.DigitalWrite(port="+str(port)+",DataLine="+str(dataline)+",value="+str(v)+")"
            self.stack.send_raw(sendstring.encode('utf-8'))
            return(None)
        else:
            return(None)

    def selftest(self):
        self.init()
        print("Setting all digital lines to 1")
        for i in (1,2,3,4,5,6):
            self.digital_write(i,"A",1)
            self.digital_write(i,"B",1)

        print("port status:")
        print("1:"+str(self.digital_read(1,"A"))+" "+str(self.digital_read(1,"B")))
        print("2:"+str(self.digital_read(2,"A"))+" "+str(self.digital_read(2,"B")))
        print("3:"+str(self.digital_read(3,"A"))+" "+str(self.digital_read(3,"B")))
        print("4:"+str(self.digital_read(4,"A"))+" "+str(self.digital_read(4,"B")))
        print("5:"+str(self.digital_read(5,"A"))+" "+str(self.digital_read(5,"B")))
        print("6:"+str(self.digital_read(6,"A"))+" "+str(self.digital_read(6,"B")))

        for i in (1,2,3,4,5,6):
            print("Analog "+str(i)+":"+str(self.analog_read(i)))

        print("Setting all digital lines to 0")
        for i in (1,2,3,4,5,6):
            self.digital_write(i,"A",0)
            self.digital_write(i,"B",0)

        time.sleep(1)

        print("Setting all digital lines to 1")
        for i in (1,2,3,4,5,6):
            self.digital_write(i,"A",1)
            self.digital_write(i,"B",1)

        time.sleep(1)

        print("Setting all digital lines back to 0")
        for i in (1,2,3,4,5,6):
            self.digital_write(i,"A",0)
            self.digital_write(i,"B",0)

