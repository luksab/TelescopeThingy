import struct
import time
import socket, select
from math import *

M_PI =  3.1415926535897932385
class SS:    
    def __init__(self,coord):
        self.coord = coord
        self.current_position = []
        self.open_sockets = []
        self.listening_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        self.listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listening_socket.bind( ("", 10001) )
        self.listening_socket.listen(5)

    hasStopped = False
    def run(self):
        while not self.hasStopped:
            # Waits for I/O being available for reading from any socket object.
            rlist, wlist, xlist = select.select( [self.listening_socket] + self.open_sockets, [], [] )
            for i in rlist:
                if i is self.listening_socket:
                    new_socket, addr = self.listening_socket.accept()
                    self.open_sockets.append(new_socket)
                    print("NEW")
                else:
                    data = i.recv(1024)
                    #print(data)
                    if data == "":
                        self.open_sockets.remove(i)
                        print("Connection closed")
                    else:
                        try:
                            print(data)
                            data = struct.unpack("3iIi", data)
                            #print("%x, %o" % (data[3], data[3]))
                            ra = data[3]*(M_PI/0x80000000)
                            dec = data[4]*(M_PI/0x80000000)
                            print(ra,dec)
                            self.coord[0] = ra
                            self.coord[1] = dec
                            
                            #reply = struct.pack("3iIii", 24, 0, time.time(), data[3], data[4], 0)
                            #print repr(reply)
                            #i.send(reply)
                        except Exception as e:
                            pass()
                            #print("StellariumServer is confused")
                            #print("StellariumServer is confused:", e)
                            #self.hasStopped = True
