import time, threading, math,StSerial as St, serial, Winkel as Wi, StellariumServer as SS#, ctypes
#import gpsThread, parallel as pa, RPi.GPIO as GPIO

#libc = ctypes.CDLL('libc.so.6')

St1s = 18
St1d = 16
St2s = 11
St2d = 13

#def delay(ms):
#  ms = int(ms*1000)
#  libc.usleep(ms)
def delay(ms):
  time.sleep(ms/1000)

def stop():
  #gpsp.running = False
  Stepper1.hasStopped = True
  Stepper2.hasStopped = True
  WCalc.hasStopped = True
  #gpsp.join()
  #StepThread1.join()
  #StepThread2.join()
  #GPIO.cleanup()
  WinkelThread.join()
  print('bye!')

##p = pa.parr()
##while not p.calc():
##  delay(100)

print('Hi!')
time.sleep(0)
print('press strg+c to exit')

coord = [0,0]
ss = SS.SS(coord)

WCalc = Wi.Winkel(1.42,0.7,time.time()*1000,56)
#gpsp  = gpsThread.GpsPoller()

s = serial.Serial('COM1',115200,timeout=0)

Stepper1 = St.Stepper('A',s)
Stepper2 = St.Stepper('B',s)
#Stepper1 = St.Stepper(St1s,St1d)
##StepThread1 = threading.Thread(target=Stepper1.run)
##StepThread1.start()
#Stepper2 = St.Stepper(St2s,St2d)
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
      print(coord[0],"  ",coord[1])
      #print('1: ',Stepper1.goalW - Stepper1.currentW)
      #print('2: ',Stepper2.goalW - Stepper2.currentW)
      #print('latitude    ' , gpsp.gpsd.fix.latitude)
      #print('longitude   ' , gpsp.gpsd.fix.longitude)
      #print('time   ' , gpsp.getSeconds())
      delay(10)
except KeyboardInterrupt:
    stop()
