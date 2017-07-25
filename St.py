import time, threading, ctypes, RPi.GPIO as GPIO, math
libc = ctypes.CDLL('libc.so.6')
def delay(ms):
  ms = int(ms*1000)
  libc.usleep(ms)
class Stepper:
  hasStopped = False
  Sts = 8
  Std = 10
  currentW = 1.5
  goalW = 0
  def __init__(self,Sts, Std):
    GPIO.setmode(GPIO.BOARD)
    self.Sts = Sts
    self.Std = Std
    GPIO.setup(Sts, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(Std, GPIO.OUT, initial=GPIO.LOW)
  def run(self):
    while not self.hasStopped:
      if abs(self.currentW - self.goalW) > 0.0015:
        if(self.currentW - self.goalW < 0):
          self.Step(1)
          self.currentW += 0.001
        else:
          self.Step(0)
          self.currentW -= 0.001
      delay(1/200)
  def Step(self,direction = 1):
    #print('S ', self.Sts,' D ',direction)
    GPIO.output(self.Std, direction)
    GPIO.output(self.Sts, 1)
    delay(1)
    GPIO.output(self.Sts, 0)
