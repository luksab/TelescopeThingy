import time, threading, ctypes, RPi.GPIO as GPIO, math, St, Winkel as Wi

libc = ctypes.CDLL('libc.so.6')

St1s = 8
St1d = 10
St2s = 11
St2d = 12

def delay(ms):
  ms = int(ms*1000)
  libc.usleep(ms)

print('Hi!')
print('press strg+c to exit')

WCalc = Wi.Winkel(1.42,0.7,time.time(),56)

Stepper1 = St.Stepper(St1s,St1d)
StepThread1 = threading.Thread(target=Stepper1.run)
StepThread1.start()
Stepper2 = St.Stepper(St2s,St2d)
StepThread2 = threading.Thread(target=Stepper2.run)
StepThread2.start()
WinkelThread = threading.Thread(target=WCalc.run)
WinkelThread.start()
try:
    while True:
      Stepper1.goalW = WCalc.goalW1
      Stepper2.goalW = WCalc.goalW2
      print('1: ',Stepper1.goalW - Stepper1.currentW)
      print('2: ',Stepper2.goalW - Stepper2.currentW)
      delay(10)
except KeyboardInterrupt:
    Stepper1.hasStopped = True
    Stepper2.hasStopped = True
    WCalc.hasStopped = True
    StepThread1.join()
    StepThread2.join()
    GPIO.cleanup()
    WinkelThread.join()
    print('bye!')
