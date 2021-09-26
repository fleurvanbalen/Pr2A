import RUStack5
__pdoc__={}
__pdoc__['PaHUB.selftest']=False

class PaHUB():
    '''
    Support for the M5Stack PaHUB unit. After setting the port with the `set_port() method`, all I2C data is routed through this port on the hub.
    '''
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent

    def set_port(self,v):
        '''
        Set the hub to a specific port.
        '''
        sendstring=">PaHUB.SetPort(port="+str(v)+")"
        self.stack.send_raw(sendstring.encode('utf-8'))


    def disable(self):
        '''
        Disable the hub.
        '''
        if (self.stack.connected):
            response=self.stack.send_raw(b">PaHUB.Disable()")
        else:
            return(None)

    def initialize(self):
        '''
        Initialize the hub.
        '''
        if (self.stack.connected):
            response=self.stack.send_raw(b">PaHUB.Initialize()")
        else:
            return(None)


    def selftest(self):
        self.set_port(3)
        self.disable()





