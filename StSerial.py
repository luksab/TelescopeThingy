import time, threading, ctypes, math, serial
libc = ctypes.CDLL('libc.so.6')
def delay(ms):
  ms = int(ms*1000)
  libc.usleep(ms)
class Stepper:
  hasStopped = False
  def __init__(self,Axis,Port):
    self.Axis = Axis
    self.currentW = 1.5
    self.goalW = 0
    self.ser = serial.Serial(Port,115200)
  def run(self):
    while not self.hasStopped:
      if abs(self.currentW - self.goalW) > 0.0030:
        if(self.currentW - self.goalW < 0):
          self.Step(1)
          self.currentW += 0.002
        else:
          self.Step(0)
          self.currentW -= 0.002
      delay(1/200)
  def runOnce(self):
    if abs(self.currentW - self.goalW) > 0.0030:
        if(self.currentW - self.goalW < 0):
          self.Step(1)
          self.currentW += 0.002
        else:
          self.Step(0)
          self.currentW -= 0.002
  def Step(self,direction = 1):
    print('Step')
    if(direction is 0 and self.Axis is 'A'):
      self.ser.write(b'x')
    elif(direction is 0 and self.Axis is 'B'):
      self.ser.write(b'y')
    elif(direction is 1 and self.Axis is 'A'):
      self.ser.write(b'X')
    elif(direction is 1 and self.Axis is 'B'):
      self.ser.write(b'Y')
#s=Stepper('A','/dev/ttyUSB0')
#while(True):
#  s.Step()
#  delay(500)
