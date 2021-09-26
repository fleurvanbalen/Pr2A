import RUStack5
from RUStack5.Tools import *
import webbrowser

__pdoc__={}
__pdoc__['GPS.selftest']=False
__pdoc__['GPS.read_timestring']=False
__pdoc__['GPS.read_datestring']=False
__pdoc__['GPS.read_latitude']=False
__pdoc__['GPS.read_longitude']=False
__pdoc__['GPS.read_satellites']=False
__pdoc__['GPS.read_altitude']=False
__pdoc__['GPS.read_speed']=False
__pdoc__['GPS.timesplit']=False
__pdoc__['GPS.timelist']=False



class GPS():
    '''
    Support for the AT6558 external GPS module.
    '''
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._timestring=""
        self._hour=0
        self._minute=0
        self._second=0
        self._latitude=0
        self._longitude=0
        self._satellites=0
        self._altitude=0
        self._speed=0
        self._time=0,0,0
        self._date=""


    def read_timestring(self):
        if (self.stack.connected):
            return Response_to_string(self.stack.send_raw(b">AT6558.GetValue(time)"))
        else:
            return("-1:-1:-1")

    def read_datestring(self):
        if (self.stack.connected):
            return Response_to_string(self.stack.send_raw(b">AT6558.GetValue(date)"))
        else:
            return("00/00/0000")

    def read_latitude(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw(b">AT6558.GetValue(latitude)"))
        else:
            return(-99999)

    def read_longitude(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw(b">AT6558.GetValue(longitude)"))
        else:
            return(-99999)

    def read_satellites(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw(b">AT6558.GetValue(satellites)"))
        else:
            return(-99999)

    def read_altitude(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw(b">AT6558.GetValue(altitude)"))
        else:
            return(-99999)

    def read_speed(self):
        if (self.stack.connected):
            return Response_to_float(self.stack.send_raw(b">AT6558.GetValue(speed)"))
        else:
            return(-99999)

    def timesplit(self,s):
        hr=-1
        mn=-1
        sec=-1
        try:
            hr,mn,sec=s.split(":")
        except:
            pass
        return(hr,mn,sec)

    @property
    def timestring(self):
        '''
        Returns the current GPS time as a string "hh:mm:ss".
        '''
        return self.read_timestring()

    @property
    def timelist(self):
        s=self.read_timestring()
        return self.timesplit(s)

    @property
    def hour(self):
        '''
        Returns the hours-part of the current GPS time.
        '''
        s=self.read_timestring()
        hr,mn,sec=self.timesplit(s)
        return hr

    @property
    def minute(self):
        '''
        Returns the minutes-part of the current GPS time.
        '''
        s=self.read_timestring()
        hr,mn,sec=self.timesplit(s)
        return mn

    @property
    def second(self):
        '''
        Returns the seconds-part of the current GPS time.
        '''
        s=self.read_timestring()
        hr,mn,sec=self.timesplit(s)
        return sec

    @property
    def longitude(self):
        '''
        Returns the current longitude.
        '''

        return self.read_longitude()
    @property
    def latitude(self):
        '''
        Returns the current latitude.
        '''
        return self.read_latitude()
    @property
    def altitude(self):
        '''
        Returns the current altitude. For geometric reasons, this may be imprecise.
        '''
        return self.read_altitude()
    @property
    def speed(self):
        '''
        Returns the current speed.
        '''
        return self.read_speed()
    @property
    def satellites(self):
        '''
        Returns the number of satellites currently used to determine your location.
        '''
        return self.read_sattelites()
    @property
    def date(self):
        '''
        Returns the current date as a string "dd/mm/yyyy".
        '''
        return self.read_datestring()




    def selftest(self):
        print(self.timestring)
        print(self.timelist)
        print(self.hour)
        print(self.minute)
        print(self.second)
        print(self.longitude)
        print(self.latitude)
        print(self.altitude)
        print(self.speed)

        self._hour=0
        self._minute=0
        self._second=0
        self._latitude=0
        self._longitude=0
        self._satellites=0
        self._altitude=0
        self._speed=0

    def where_am_i(self):
        '''
        Launches your webbrowser and shows you where you are using your current GPS location.
        '''
        print("Opening webbrowser to show you where you are...")
        lat=self.latitude
        lon=self.longitude
        s="https://www.google.nl/maps/@"+str(lat)+","+str(lon)+",14z"
        webbrowser.open(s, autoraise=True)
