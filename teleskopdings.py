import time, threading, math,StSerial as St
import serial, Winkel as Wi, StellariumServer as SS

def delay(ms):
  time.sleep(ms/1000)

def stop():
  Stepper1.hasStopped = True
  Stepper2.hasStopped = True
  WCalc.hasStopped = True
  WinkelThread.join()
  print('bye!')

print('Hi!')
print('press strg+c to exit')

coord = [0,0]
ss = SS.SS(coord)

WCalc = Wi.Winkel(1.42,0.7,time.time()*1000,56)

s = serial.Serial('COM1',115200,timeout=0)

Stepper1 = St.Stepper('A',s)
Stepper2 = St.Stepper('B',s)
WinkelThread = threading.Thread(target=WCalc.run)
WinkelThread.start()
SSThread = threading.Thread(target=ss.run)
SSThread.start()
try:
    while True:
      Stepper1.goalW = WCalc.goalW1
      Stepper2.goalW = WCalc.goalW2
      Stepper1.runOnce()
      Stepper2.runOnce()
      print(coord[0],"  ",coord[1])
      delay(10)
except KeyboardInterrupt:
    stop()
