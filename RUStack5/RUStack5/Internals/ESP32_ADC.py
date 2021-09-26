import time
import RUStack5
from RUStack5.Tools import *
__pdoc__={}
__pdoc__['ESP32_ADC.grab_string'] = False
__pdoc__['ESP32_ADC.read_gpio35'] = False
__pdoc__['ESP32_ADC.read_gpio36'] = False
__pdoc__['ESP32_ADC.selftest'] = False

class ESP32_ADC:
    def __init__(self,RUStack_parent):
        """
        Support for the M5Stack's internal Analog to Digital converter (ADC).
        """
        self.stack=RUStack_parent
        self.ATT_TABLE = (
            (0,b">ESP32ADC.Configure(Attenuation=0db)"),
            (2.5,b">ESP32ADC.Configure(Attenuation=2.5db)"),
            (6,b">ESP32ADC.Configure(Attenuation=6db)"),
            (11,b">ESP32ADC.Configure(Attenuation=11db)"))


    def get_configuration(self):
        if (self.stack.connected):
            names=[
            "ports",
            "samplingrate",
            "samplesize",
            "measuring_interval",
            "trigger_event",
            "attenuation",
            "output_in_byte",
            "mark_channel_two",
                ]
            response=self.stack.send_raw_multiline(b">ESP32ADC.GetConfiguration()")
            lines=[]
            for i in response:
                i_str=i.decode('UTF-8')
                stripped=i_str.replace("\r\n","").replace(" ","")
                splitted=stripped.split(":")
                lines.append(splitted)
            return {names[i]: lines[i][1] for i in range(0, len(lines)-1)}




            dict={
            1:2,
            3:4


            }

            return response
        else:
            return(None)



    def set_attenuation(self,r):
        """
        Set the attenuation of the ADC's prescaler. Valid values (in units of dB) are 0, 2.5, 6 and 11.
        """
        for (range, sendstring) in self.ATT_TABLE:
            if range==r:
                self.stack.send_raw(sendstring)
                self.gain=r
                self._att = r
                break


    def read_gpio35(self):
        if (self.stack.connected):
            self.stack.send_raw(b">ESP32ADC.Configure(port=35)")
            response=self.stack.send_raw(b">ESP32ADC.GetValue()")
            return Response_to_float(response)
        else:
            return(None)

    def read_gpio36(self):
        if (self.stack.connected):
            self.stack.send_raw(b">ESP32ADC.Configure(port=36)")
            response=self.stack.send_raw(b">ESP32ADC.gpio36()")
            return Response_to_float(response)
        else:
            return(None)

    def read_both_gpios(self):
        if (self.stack.connected):
            self.stack.send_raw(b">ESP32ADC.Configure(port=both)")
            response=self.stack.send_raw(b">ESP32ADC.GetValue()")
            return Response_to_float_list(response)
        else:
            return(None)



    def read_envelope_gpio35(self,measuring_interval:int):
        '''
        Read ADC-values from pin 36 during a specific time interval, measurement_time (in ms). Return the highest value minus the lowest value measured during that time interval.
        '''
        if (self.stack.connected):
            self.stack.send_raw(b">ESP32ADC.Configure(port=35,MeasuringInterval="+str(measuring_interval)+")")
            sendstring=">ESP32ADC.GetEnvelope()"
            response=self.stack.send_raw(sendstring.encode('utf-8'))
            return Response_to_float_list(response)
        else:
            return(None)

    def read_envelope_gpio36(self,measuring_interval:int):
        '''
        Read ADC-values from pin 36 during a specific time interval, measurement_time (in ms). Return the highest value minus the lowest value measured during that time interval.
        '''
        if (self.stack.connected):
            self.stack.send_raw(b">ESP32ADC.Configure(port=36,MeasuringInterval="+str(measuring_interval)+")")
            sendstring=">ESP32ADC.GetEnvelope()"
            response=self.stack.send_raw(sendstring.encode('utf-8'))
            #return Response_to_float_list(response)
            return response
        else:
            return(None)

    def read_envelope_both(self,measuring_interval:int):
        '''
        Read ADC-values from pin 35&36 during a specific time interval, measurement_time (in ms). Return the highest value minus the lowest value measured during that time interval.
        '''
        if (self.stack.connected):
            self.stack.send_raw(b">ESP32ADC.Configure(port=both,MeasuringInterval="+str(measuring_interval)+")")
            sendstring=">ESP32ADC.GetValue()"
            response=self.stack.send_raw(sendstring.encode('utf-8'))
            return Response_to_float_list(response)
        else:
            return(None)



    def acquire_samples(self,port:int,nos:int,sps:int,trigger:str)->list:
        '''
        Acquire a series of samples from the specified port. Parameters are:\n
        port -> GPIO pin to acquire from, valid values are 35 and 36.\n
        nos -> number of samples to acquire.\n
        sps -> samples per second.\n
        trigger -> event on pin 5 that starts the measurement. Valid values are: 'Low','High','Change','Rising','Falling','Ignore'. If set to 'Ignore', measurement starts immediately.\n
        Returns a list of measured values.
        '''
        sendstring=">ESP32ADC.Configure(Port="+str(port)+", SampleSize="+str(nos)+", SamplingRate="+str(sps)+", TriggerEvent="+trigger+")"
        self.stack.send_raw(sendstring.encode('utf-8'))
        self.stack.send_raw_wait_read(b">ESP32ADC.AcquireToBuffer()")
        values=self.stack.send_raw_read_n_words(b'>ESP32ADC.GetBuffer()',nos)
        return values

    def acquire_samples_both_ports(self,nos:int,sps:int,trigger:str)->list:
        '''
        Acquire a series of samples from port 35 and 36 simultaneously.\n
        nos -> number of samples to acquire.\n
        sps -> samples per second.\n
        trigger -> event on pin 5 that starts the measurement. Valid values are: 'Low','High','Change','Rising','Falling','Ignore'. If set to 'Ignore', measurement starts immediately.\n
        Returns a tuple with two lists of measured values (data_35[],data_36[]).
        '''

        sendstring=">ESP32ADC.Configure(Port=both"+", SampleSize="+str(2*nos)+", SamplingRate="+str(sps)+", TriggerEvent="+trigger+")"
        self.stack.send_raw(sendstring.encode('utf-8'))

        self.stack.send_raw_wait_read(b">ESP32ADC.AcquireToBuffer()")
        values=self.stack.send_raw_read_n_words(b'>ESP32ADC.GetBuffer()',2*nos)
        values35=values[::2]
        values36=values[1::2]
        return values35,values36


#        streaming

    def start_single_stream(self,p:int,sps:int,trigger:str):
        '''
        Sends a request to the M5Stack to start streaming ADC data.
        '''

        sendstring=">ESP32ADC.Configure(Port="+str(p)+", SamplingRate="+str(sps)+", TriggerEvent="+trigger+", format=byte)"
        self.stack.send_raw(sendstring.encode('utf-8'))

        sendstring=">ESP32ADC.GetStream()"
        self.stack.send_raw(sendstring.encode('utf-8'))

    def read_sample_from_single_stream(self):
        return self.stack.read_word()

    def stop_single_stream(self):
        self.stack.send_raw(b' ')


    def start_dual_stream(self,p:int,sps:int,trigger:str):
        '''
        Sends a request to the M5Stack to start streaming ADC data.
        '''
        sendstring=">ESP32ADC.Configure(Port=both, MarkChannelTwo=true, SamplingRate="+str(sps)+", TriggerEvent="+trigger+", format=byte)"
        self.stack.send_raw(sendstring.encode('utf-8'))

        sendstring=">ESP32ADC.GetStream()"
        self.stack.send_raw(sendstring.encode('utf-8'))

    def read_sample_from_dual_stream(self):
        first=self.stack.read_word()
        second=self.stack.read_word()
        if (first<4096):
            val35=first
            val36=second
        else:
            val35=second
            val36=first
        return(val35,val36)

    def stop_dual_stream(self):
        self.stack.send_raw(b' ')




