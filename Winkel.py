from sympy import *
import math, time#, ctypes
#libc = ctypes.CDLL('libc.so.6')
#def delay(ms):
#  ms = int(ms*1000)
#  libc.usleep(ms)
def delay(ms):
  time.sleep(ms/1000)
class Winkel:
    def calcW(self,a, b, c, d):
        alpha  = a
        beta   = b
        epsilon= c/(12 * 3600) * math.pi
        phi    = math.radians(d)
        gamma = self.Ce
        delta = self.Cf
        P = Matrix([math.sin(beta), math.cos(beta), math.sin(alpha)])
        R = Matrix([[math.cos(epsilon), -math.sin(phi)*math.sin(epsilon), math.cos(phi)*math.sin(epsilon)], [math.sin(phi)*math.sin(epsilon), (((math.cos(phi))**2)*(1-math.cos(epsilon)))+math.cos(epsilon), math.cos(phi)*math.sin(phi)*(1-math.cos(epsilon))], [-math.cos(phi)*math.sin(epsilon), math.sin(phi)*math.cos(phi)*(1-math.cos(epsilon)), (((math.sin(phi))**2)*(1-math.cos(epsilon)))+math.cos(epsilon)]])
        S = R*P
        Y = ([0, 1/(math.cos(delta)), math.sin(gamma)])
        N = Matrix([-math.sin(gamma)*math.sin(delta), -math.sin(gamma)*math.cos(delta), 1])
        c = math.acos((P.T*Y)/((math.hypot(1, P[2]))*(math.hypot(Y[1], Y[2]))))
        goalW1 = math.pi/2 - math.acos((P.T*N)/((math.hypot(1, P[2]))*(math.sqrt((N[0]**2)+(N[1]**2)+1))))
        goalW2 = math.acos(math.cos(goalW1)*math.cos(c)+math.sin(goalW1)*math.sin(c)*math.tan(goalW1)*math.cot(c))
        #self.s1 = ((math.sin(beta) * math.cos(alpha) * math.cos(epsilon))
        #    - (math.cos(beta) * math.cos(alpha) * math.sin(phi) * math.sin(epsilon))
        #    + (math.sin(alpha) * math.cos(phi) * math.sin(epsilon)))
        #self.s2 = ((math.sin(beta) * math.cos(alpha) * math.sin(phi) * math.sin(epsilon))
        #    + (math.cos(beta) * math.cos(alpha) * ((math.pow(math.cos(phi),2) * (1 - math.cos(epsilon))) + math.cos(epsilon)))
        #    + (math.sin(alpha) * math.cos(phi) * math.sin(phi) * (1 - math.cos(epsilon))))
        #self.s3 = (- (math.sin(beta) * math.cos(alpha) * math.cos(phi) * math.cos(epsilon))
        #    + (math.cos(beta) * math.cos(alpha) * math.sin(phi) * math.cos(phi) * (1 - math.cos(epsilon))) 
        #    + (math.sin(alpha) * ((math.pow(math.sin(phi),2) * (1 - math.cos(epsilon)) + math.cos(epsilon)))))
        #if not self.s2 == 0:
        #   self.goalW2 = math.atan(self.s1/self.s2)
        #if not self.s2 == 0 or not self.s2 == 0:
        #    self.goalW1 = math.atan(self.s3/math.hypot(self.s1,self.s2))
        #print(s1)
        #print(s2)
        #print(s3)
        #print(self.goalW1)
        #print(self.goalW2)
    def calc(self,a, b, c, d):
      alpha  = a
      beta   = b
      epsilon= c/(12 * 3600) * math.pi
      phi    = math.radians(d)
      self.s1 = ((math.sin(beta) * math.cos(alpha) * math.cos(epsilon))
          - (math.cos(beta) * math.cos(alpha) * math.sin(phi) * math.sin(epsilon))
          + (math.sin(alpha) * math.cos(phi) * math.sin(epsilon)))
      self.s2 = ((math.sin(beta) * math.cos(alpha) * math.sin(phi) * math.sin(epsilon))
          + (math.cos(beta) * math.cos(alpha) * ((math.pow(math.cos(phi),2) * (1 - math.cos(epsilon))) + math.cos(epsilon)))
          + (math.sin(alpha) * math.cos(phi) * math.sin(phi) * (1 - math.cos(epsilon))))
      self.s3 = (- (math.sin(beta) * math.cos(alpha) * math.cos(phi) * math.cos(epsilon))
          + (math.cos(beta) * math.cos(alpha) * math.sin(phi) * math.cos(phi) * (1 - math.cos(epsilon))) 
          + (math.sin(alpha) * ((math.pow(math.sin(phi),2) * (1 - math.cos(epsilon)) + math.cos(epsilon)))))
      if not self.s2 == 0:
          self.goalW2 = math.atan(self.s1/self.s2)
      if not self.s2 == 0 or not self.s2 == 0:
          self.goalW1 = math.atan(self.s3/math.hypot(self.s1,self.s2))
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
