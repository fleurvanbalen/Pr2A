import RUStack5
from RUStack5.Tools import *

__pdoc__={}
__pdoc__['IMU.read_acc'] = False
__pdoc__['IMU.read_gyro'] = False
__pdoc__['IMU.read_pitch'] = False
__pdoc__['IMU.read_roll'] = False
__pdoc__['IMU.read_yaw'] = False
__pdoc__['IMU.selftest'] = False


class IMU():
    """
    This class provides support for the M5Stack Grey's internal Inertial Measurement Unit (IMU). With this peripheral it's possible to measure the three components of the acceleration vector and the three componentes of the instantaneous rotation vector. Three derived variables are available, pitch, roll and yaw, indicating the absolute orientation in space. However, these variables are prone to drift and of limited use. Two methods are available to set the appropriate dynamic range of the accelerometer/gyroscope. Note that the acceleration due to gravity is included in the readings provided by the accelerometer. For more information, consult the datasheet: https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/core/MPU-6886-000193%2Bv1.1_GHIC_en.pdf
    """
    def __init__(self,RUStack_parent):
        self.stack=RUStack_parent
        self._accX=0
        self._accY=0
        self._accZ=0
        self._gyroX=0
        self._gyroY=0
        self._gyroZ=0
        self._pitch=0
        self._roll=0
        self._yaw=0
        self.GYRO_RANGETABLE = (
            (250,b">M5Gyroscope.Configure(scalefactor=250DPS)"),
            (500,b">M5Gyroscope.Configure(scalefactor=500DPS)"),
            (1000,b">M5Gyroscope.Configure(scalefactor=1000DPS)"),
            (2000,b">M5Gyroscope.Configure(scalefactor=2000DPS)"))
        self.ACC_RANGETABLE = (
            (2,b">M5Accelerometer.Configure(scalefactor=2g)"),
            (4,b">M5Accelerometer.Configure(scalefactor=4g)"),
            (8,b">M5Accelerometer.Configure(scalefactor=8g)"),
            (16,b">M5Accelerometer.Configure(scalefactor=16g)"))

    # Accelerometer
    def read_acc(self,coord):
        if (self.stack.connected):
            sendstring=">M5Accelerometer.GetValue("+coord+")"
            response=self.stack.send_raw(sendstring.encode('UTF-8'))
            return Response_to_float(response)
        else:
            return(None)
    @property
    def accX(self):
        '''The x-component of the acceleration vector'''
        return self.read_acc('X')
    @property
    def accY(self):
        '''The y-component of the acceleration vector'''
        return self.read_acc('Y')
    @property
    def accZ(self):
        '''The z-component of the acceleration vector'''
        return self.read_acc('Z')
    def set_acc_range(self,r):
        '''
        Sets the measurement range of the accelerometer. Valid values (in units of g) are 2,4,8,16.
        '''

        for (range, sendstring) in self.ACC_RANGETABLE:
            if range==r:
                self.stack.send_raw(sendstring)
                break

    # Gyro
    def read_gyro(self,coord):
        if (self.stack.connected):
            sendstring=">M5Gyroscope.GetValue("+coord+")"
            response=self.stack.send_raw(sendstring.encode('UTF-8'))
            return Response_to_float(response)
        else:
            return(None)
    @property
    def gyroX(self):
        '''The x-component of the rotation vector'''
        return self.read_gyro('X')
    @property
    def gyroY(self):
        '''The y-component of the rotation vector'''
        return self.read_gyro('Y')
    @property
    def gyroZ(self):
        '''The z-component of the rotation vector'''
        return self.read_gyro('Z')
    def set_gyro_range(self,r):
        '''
        Sets the measurement range of the gyroscope. Valid values (in degrees per second) are 250,500,1000,2000.
        '''
        for (range, sendstring) in self.GYRO_RANGETABLE:
            if range==r:
                self.stack.send_raw(sendstring)
                break



    def selftest(self):
        print("set acc&gyro ranges:")
        self.set_acc_range(2)
        self.set_acc_range(4)
        self.set_acc_range(8)
        self.set_acc_range(16)

        self.set_gyro_range(250)
        self.set_gyro_range(500)
        self.set_gyro_range(1000)
        self.set_gyro_range(2000)

        print("accelerometers:")
        print(self.accX)
        print(self.accY)
        print(self.accZ)

        print("gyros:")
        print(self.gyroX)
        print(self.gyroY)
        print(self.gyroZ)

        print("pitch roll yaw:")
        print(self.pitch)
        print(self.roll)
        print(self.yaw)

