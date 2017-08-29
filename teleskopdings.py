import time, threading, ctypes, math,StSerial as St, Winkel as Wi
#import gpsThread, parallel as pa, RPi.GPIO as GPIO

libc = ctypes.CDLL('libc.so.6')

St1s = 18
St1d = 16
St2s = 11
St2d = 13

def delay(ms):
  ms = int(ms*1000)
  libc.usleep(ms)

##p = pa.parr()
##while not p.calc():
##  delay(100)

print('Hi!')
time.sleep(3)
print('press strg+c to exit')

WCalc = Wi.Winkel(1.42,0.7,time.time()*1000,56)
#gpsp  = gpsThread.GpsPoller()

Stepper1 = St.Stepper('A','/dev/ttyUSB0')
Stepper2 = St.Stepper('B','/dev/ttyUSB0')
#Stepper1 = St.Stepper(St1s,St1d)
##StepThread1 = threading.Thread(target=Stepper1.run)
##StepThread1.start()
#Stepper2 = St.Stepper(St2s,St2d)
##StepThread2 = threading.Thread(target=Stepper2.run)
##StepThread2.start()
WinkelThread = threading.Thread(target=WCalc.run)
WinkelThread.start()
try:
    #gpsp.start()
    while True:
      Stepper1.goalW = WCalc.goalW1
      Stepper2.goalW = WCalc.goalW2
      Stepper1.runOnce()
      Stepper2.runOnce()
      #print('1: ',Stepper1.goalW - Stepper1.currentW)
      #print('2: ',Stepper2.goalW - Stepper2.currentW)
      #print('latitude    ' , gpsp.gpsd.fix.latitude)
      #print('longitude   ' , gpsp.gpsd.fix.longitude)
      #print('time   ' , gpsp.getSeconds())
      delay(10)
except KeyboardInterrupt:
    #gpsp.running = False
    Stepper1.hasStopped = True
    Stepper2.hasStopped = True
    WCalc.hasStopped = True
    #gpsp.join()
    #StepThread1.join()
    #StepThread2.join()
    GPIO.cleanup()
    WinkelThread.join()
    print('bye!')
