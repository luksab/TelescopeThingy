from sympy import *
import math, time, ctypes
libc = ctypes.CDLL('libc.so.6')
def delay(ms):
  ms = int(ms*1000)
  libc.usleep(ms)
#def delay(ms):
#  time.sleep(ms/1000)
class Winkel:
    def 
    def __init__(self,alpha = 1.5,beta = 1,StartTime = time.time(),phi = 45):
        self.s1 = 5
        self.s2 = 5
        self.s3 = 5
        self.goalW1 = math.pi / 2
        self.goalW2 = math.pi / 2
        self.hasStopped = False
        self.Ca = alpha
        self.Cb = beta
        self.Cc = StartTime
        self.Cd = phi
    def initWithNonParallel(self,alpha = 1.5,beta = 1,StartTime = time.time(),phi = 45,gamma = 0,delta = 0):
        self.s1 = 5
        self.s2 = 5
        self.s3 = 5
        self.goalW1 = math.pi / 2
        self.goalW2 = math.pi / 2
        self.hasStopped = False
        self.Ca = alpha
        self.Cb = beta
        self.Cc = StartTime
        self.Cd = phi
        self.Ce = gamma
        self.Cf = delta
    def run(self):
        while not self.hasStopped:
            self.calc(self.Ca,self.Cb,time.time()-self.Cc,self.Cd)
            delay(50)
