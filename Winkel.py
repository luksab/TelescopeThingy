import math, time, ctypes
libc = ctypes.CDLL('libc.so.6')
def delay(ms):
  ms = int(ms*1000)
  libc.usleep(ms)
class Winkel:
    s1 = 5
    s2 = 5
    s3 = 5
    goalW1 = math.pi / 2
    goalW2 = math.pi / 2
    Ca = 1.5
    Cb = 1
    Cc = 1357
    Cd = 45
    hasStopped = False
    def calcW(self,a, b, c, d):
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
        #print(s1)
        #print(s2)
        #print(s3)
        #print(self.goalW1)
        #print(self.goalW2)
    def __init__(self,alpha,beta,StartTime,phi):
        self.Ca = alpha
        self.Cb = beta
        self.Cc = StartTime
        self.Cd = phi
    def run(self):
        while not self.hasStopped:
            self.calcW(self.Ca,self.Cb,time.time()-self.Cc,self.Cd)
            delay(50)
