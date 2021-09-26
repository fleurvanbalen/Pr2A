import RUStack5
from RUStack5.Tools import *

__pdoc__={}
__pdoc__['GAS.selftest']=False
__pdoc__['GAS.read_tvoc']=False
__pdoc__['GAS.read_eco2']=False
__pdoc__['GAS.read_baseline_tvoc']=False
__pdoc__['GAS.read_baseline_eco2']=False
__pdoc__['GAS.read_h2']=False
__pdoc__['GAS.read_ethanol']=False


class GAS():
    '''
    Support for the SGP30 gas sensor. For details about interpretation of the data, read the datasheet at: https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9_Gas_Sensors/Datasheets/Sensirion_Gas_Sensors_SGP30_Datasheet.pdf
    '''
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._tvoc=0
        self._eco2=0
        self._baseline_tvoc=0
        self._baseline_eco2=0
        self._h2=0
        self._ethanol=0

    def init(self):
        '''
        Initialize the sensor.
        '''
        if (self.stack.connected):
            response=self.stack.send_raw(b">SGP30.init()")
            return Response_to_float(response)
        else:
            return(None)

    def read_tvoc(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">SGP30.tvoc()")
            return(Response_to_float(response))
        else:
            return -99999

    def read_eco2(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">SGP30.eco2()")
            return(Response_to_float(response))
        else:
            return -99999

    def read_baseline_tvoc(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">SGP30.baseline-tvoc()")
            return(Response_to_float(response))
        else:
            return -99999

    def read_baseline_eco2(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">SGP30.baseline-eco2()")
            return(Response_to_float(response))
        else:
            return -99999

    def read_h2(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">SGP30.h2()")
            return(Response_to_float(response))
        else:
            return -99999

    def read_ethanol(self):
        if (self.stack.connected):
            response=self.stack.send_raw(b">SGP30.ethanol()")
            return(Response_to_float(response))
        else:
            return -99999


    def selftest(self):
        self.init()
        print(self.tvoc)
        print(self.eco2)
        print(self.baseline_tvoc)
        print(self.baseline_eco2)
        print(self.h2)
        print(self.ethanol)

    @property
    def tvoc(self):
        '''
        Returns the current concentration of Total Volatile Organic Compounds (TVOC)
        '''
        tvoc=self.read_tvoc()
        return(tvoc)

    @property
    def baseline_tvoc(self):
        '''
        Returns the current baseline concentration of Total Volatile Organic Compounds (TVOC)
        '''

        baseline_tvoc=self.read_baseline_tvoc()
        return(baseline_tvoc)

    @property
    def eco2(self):
        '''
        Returns the current concentration of Carbon Dioxide (CO2)
        '''
        eco2=self.read_eco2()
        return(eco2)

    @property
    def baseline_eco2(self):
        '''
        Returns the current baseline concentration of Carbon Dioxide (CO2)
        '''
        baseline_eco2=self.read_baseline_eco2()
        return(baseline_eco2)

    @property
    def h2(self):
        '''
        Returns the current concentration of hydrogen (H2)
        '''
        h2=self.read_h2()
        return(h2)

    @property
    def ethanol(self):
        '''
        Returns the current concentration of ethanol.
        '''
        ethanol=self.read_ethanol()
        return(ethanol)
