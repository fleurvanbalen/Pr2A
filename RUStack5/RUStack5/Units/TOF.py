import RUStack5
from RUStack5.Tools import *

class TOF():
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent

    def get_distance(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">TOF.GetDistance()")
            return Response_to_float(response)
        else:
            return(None)

    def enable_long_range(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">TOF.Configure(LongRange=true)")
        else:
            return(None)

    def enable_high_accuracy(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">TOF.Configure(HighAccuracy=true")
        else:
            return(None)

    def init(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">TOF.Initialize()")
        else:
            return(None)

    def get_buffer_as_string(self):
        response=self.stack.send_raw_multiline(b">TOF.GetBuffer(format=STRING)")
        return response


    def get_buffered_data(self,mt,sr):
        self.stack.send_raw(b">TOF.Configure(IncludeTimestamps=false)")
        sendstring=">TOF.AcquireToBuffer(measuretime="+str(mt)+", SamplingRate="+str(sr)+")"
        words_to_read=self.stack.send_raw_wait_read_2(sendstring.encode('utf-8'))
        values=self.stack.send_raw_read_n_words_2(b'>TOF.GetBuffer(format=BYTE)',words_to_read)
        return values

    def get_buffered_data_with_timestamps(self,mt,sr):
        self.stack.send_raw(b">TOF.Configure(IncludeTimestamps=true)")
        sendstring=">TOF.AcquireToBuffer(measuretime="+str(mt)+", SamplingRate="+str(sr)+")"
        words_to_read=self.stack.send_raw_wait_read_2(sendstring.encode('utf-8'))
        y_values=self.stack.send_raw_read_n_words_2(b'>TOF.GetBuffer(format=BYTE)',words_to_read)
        t_values=self.stack.send_raw_read_n_words_2(b'>TOF.GetBuffer(format=byte)',words_to_read)
        return t_values,y_values
