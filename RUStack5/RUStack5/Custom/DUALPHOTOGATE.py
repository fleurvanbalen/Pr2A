import RUStack5
from RUStack5.Tools import *

__pdoc__={}

class DUALPHOTOGATE():
    '''
    Support for a DUAL PHOTOGATE.
    '''
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent


    def get_pass_time(self,timeout=None):
        if (self.stack.connected):
            if timeout==None:
                s=""
            else:
                s="timeout="+str(timeout)
            sendstring=">DUALPHOTOGATE.GetTriggerEventInterval("+s+")"
            response=self.stack.send_raw_wait_for_response(sendstring.encode('utf-8'))
            return Response_to_int(response)
        else:
            return(None)



