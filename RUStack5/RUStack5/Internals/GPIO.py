import RUStack5
from RUStack5.Tools import *

class GPIO():
    """
    GPIO
    """
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent


    def get_value(self,port):
        '''
        Get the state of the specified port.
        '''
        if (self.stack.connected):
            sendstring=">M5GPIO.GetValue(port="+str(port)+")"
            response=self.stack.send_raw(sendstring.encode('UTF-8'))
            return Response_to_int(response)
        else:
            return(None)


    def set_value(self,port,value):
        '''
        Set the state of the specified port.
        '''
        sendstring=">M5GPIO.SetValue(port="+str(port)+",value="+str(value)+")"
        self.stack.send_raw(sendstring.encode('UTF-8'))
