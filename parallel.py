import smbus
import math
import time
class parr():
    power_mgmt = 0x6b
    bus = smbus.SMBus(1)
    address = 0x68
    def read_word_2c(self,reg):
        h = self.bus.read_byte_data(self.address, reg)
        l = self.bus.read_byte_data(self.address, reg+1)
        val = (h << 8) + l
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val
    def __init__(self):
        # Aktivieren, um das Modul ansprechen zu koennen
        self.bus.write_byte_data(self.address, self.power_mgmt, 0)
    def calc(self):
        bx = self.read_word_2c(0x3b)
        by = self.read_word_2c(0x3d)
        bz = self.read_word_2c(0x3f)
        print('x: ',bx,' y: ',by)
        if((abs(bx) + abs(by)) < 10):
            return True
        else:
            if(bx>10):
                print("Bein2>Bein3")
            else:
                if(bx<-10):
                    print("Bein2<Bein3")
            if(by>10):
                print("Bein1>(Bein2+Bein3)/2")
            else:
                if(by<-10):
                    print("Bein1<(Bein2+Bein3)/2")
            return False
