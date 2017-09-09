import time, threading, math,St, Winkel as Wi, StellariumServer as SS, ctypes
#import gpsThread, parallel as pa
import RPi.GPIO as GPIO
libc = ctypes.CDLL('libc.so.6')

St1s = 10
St1d = 8
St2s = 3
St2d = 5

StepsPerRotationA = 16*200*10
StepsPerRotationB = 16*200*15

def delay(ms):
  ms = int(ms*1000)
  libc.usleep(ms)

def stop():
  print('bye!')
  #gpsp.running = False
  Stepper1.hasStopped = True
  Stepper2.hasStopped = True
  WCalc.hasStopped = True
  ss.hasStopped = True
  #gpsp.join()
  #StepThread1.join()
  #StepThread2.join()
  #GPIO.cleanup()
  SSThread.join()
  WinkelThread.join()
  print('bye!(Now really)')

##p = pa.parr()
##while not p.calc():
##  delay(100)

print('Hi!')
time.sleep(3)
print('press strg+c to exit')

coord = [0,0]
ss = SS.SS(coord)

WCalc = Wi.Winkel(0,0,time.time(),50.8228)
#gpsp  = gpsThread.GpsPoller()

Stepper1 = St.Stepper(St1s,St1d,StepsPerRotationA)
##StepThread1 = threading.Thread(target=Stepper1.run)
##StepThread1.start()
Stepper2 = St.Stepper(St2s,St2d,StepsPerRotationB)
##StepThread2 = threading.Thread(target=Stepper2.run)
##StepThread2.start()
WinkelThread = threading.Thread(target=WCalc.run)
WinkelThread.start()
SSThread = threading.Thread(target=ss.run)
SSThread.start()
try:
    #gpsp.start()
    while True:
      Stepper1.goalW = WCalc.goalW1
      Stepper2.goalW = WCalc.goalW2
      Stepper1.runOnce()
      Stepper2.runOnce()
      #print(coord[0],"  ",coord[1])
      WCalc.Ca = coord[0]
      WCalc.Cb = coord[1]
      #print('1: ',Stepper1.goalW - Stepper1.currentW)
      #print('2: ',Stepper2.goalW - Stepper2.currentW)
      #print('latitude    ' , gpsp.gpsd.fix.latitude)
      #print('longitude   ' , gpsp.gpsd.fix.longitude)
      #print('time   ' , gpsp.getSeconds())
      delay(10)
except KeyboardInterrupt:
    stop()
