import os
from gps import *
from time import *
import time
import threading
import dateutil.parser as dp
 
class GpsPoller(threading.Thread):
  gpsd = None
  def __init__(self):
    threading.Thread.__init__(self)
    self.gpsd = gps.GPS(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    while self.running:
      try:
        self.gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
      except StopIteration:
        time.sleep(0.1)
  def getSeconds(self):
    return int(dp.parse(self.gpsd.utc).strftime('%s'))
