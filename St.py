import time, threading, ctypes, RPi.GPIO as GPIO, math
libc = ctypes.CDLL('libc.so.6')
def delay(ms):
  ms = int(ms*1000)
  libc.usleep(ms)
class Stepper:
  hasStopped = False
  currentW = 1.5
  goalW = 0
  def __init__(self,Sts, Std):
    GPIO.setmode(GPIO.BOARD)
    self.Sts = Sts
    self.Std = Std
    #GPIO.setup(Sts, GPIO.OUT, initial=GPIO.LOW)
    #GPIO.setup(Std, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Std, GPIO.OUT)
    GPIO.setup(Sts, GPIO.OUT)
    GPIO.output(Std, False)
    GPIO.output(Sts, False)
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
    if(direction is 0):
      direction = False
    else:
      direction = True
    #print('S ', self.Sts,' D ',direction)
    GPIO.output(self.Std, direction)
    GPIO.output(self.Sts, 1)
    delay(5)
    GPIO.output(self.Sts, 0)
    delay(5)
