from sympy import *
import datetime
import math, time, ctypes
libc = ctypes.CDLL('libc.so.6')
def delay(ms):
  ms = int(ms*1000)
  libc.usleep(ms)
#def delay(ms):
#  time.sleep(ms/1000)
class Winkel:
    def calc(self,RA, DEC, LAT, LONG): #right ascension, declination, lattitude, longitude, days since J2000, universal time
        dt = datetime.datetime.now() - self.start_time
        UT = ((dt.seconds + dt.microseconds / 1000000.0)/3600)
        self.goalW1 = math.asin(math.sin(DEC)*math.sin(LAT)+math.cos(DEC)*math.cos(LAT)*math.cos(100.46+0.985647*self.diff+LONG+15*UT-RA))
        self.goalW2 = math.acos((math.sin(DEC)-math.sin(self.goalW1)*math.sin(LAT))/(math.cos(self.goalW1)*math.cos(LAT)))
    def __init__(self,alpha = 1.5,beta = 1,LAT=51,LON=7):
        d = (datetime.date.today()-datetime.date(2000, 1, 1))
        self.diff = d.days-0.5
        d = datetime.datetime(2000,1,1)
        self.start_time = d.replace(hour=12, minute=0)
        self.s1 = 5
        self.s2 = 5
        self.s3 = 5
        self.goalW1 = math.pi / 2
        self.goalW2 = math.pi / 2
        self.hasStopped = False
        self.Ca = alpha
        self.Cb = beta
        self.Cc = LAT
        self.Cd = LON
    def initWithNonParallel(self,alpha = 0.76,beta = 1.56,LAT = 51,LON = 7,gamma = 0,delta = 0):
        self.today = datetime.date.today()
        self.s1 = 5
        self.s2 = 5
        self.s3 = 5
        self.goalW1 = math.pi / 2
        self.goalW2 = math.pi / 2
        self.hasStopped = False
        self.Ca = alpha
        self.Cb = beta
        self.Cc = LAT
        self.Cd = LON
        self.Ce = gamma
        self.Cf = delta
    def run(self):
        while not self.hasStopped:
            self.calc(self.Ca,self.Cb,self.Cc,self.Cd)
            delay(50)
