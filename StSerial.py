import time, threading, math, serial#, ctypes
#libc = ctypes.CDLL('libc.so.6')
#def delay(ms):
#  ms = int(ms*1000)
#  libc.usleep(ms)
def delay(ms):
  time.sleep(ms*1000)

class Stepper:
  hasStopped = False
  def __init__(self,Axis,ser):
    self.Axis = Axis
    self.currentW = 0
    self.goalW = 0
    self.ser = ser
  def run(self):
    while not self.hasStopped:
      time.sleep(0.5)
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
    if(direction is 0 and self.Axis is 'A'):
      self.ser.write(b'x')
      #print(self.ser.read(1))
    elif(direction is 0 and self.Axis is 'B'):
      self.ser.write(b'y')
      #print(self.ser.read(1))
    elif(direction is 1 and self.Axis is 'A'):
      self.ser.write(b'X')
      #print(self.ser.read(1))
    elif(direction is 1 and self.Axis is 'B'):
      self.ser.write(b'Y')
      #print(self.ser.read(1))
#s=Stepper('A','/dev/ttyUSB0')
#while(True):
#  s.Step()
#  delay(500)
