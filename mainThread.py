import threading
from time import sleep
import socket

class MainThread(threading.Thread):
    cache = {} # variable de clase

    def __init__(self):
        threading.Thread.__init__(self)
        self.clientSocket = None #variable de instancia

    def run(self):
        while True:
            if self.clientSocket is not None:
                print self.clientSocket.getpeername() #codigo para probar
                self.comando(self.clientSocket)
                sleep(60)
            else:
                #print "entro"
                sleep(1)

    def setClientSocket(self,s):
        self.clientSocket = s

    def getClientSocket(self):
        return self.clientSocket

    def setDict(self,key,value):
        self.cache[key]=value
        res = 'OK'
        return res

    def getDictValue(self,key):
      res = ""
      if key in self.cache:
        res = self.cache[key]
      else:
        res = 'NaN'
      return res
    
    def listCache(self,cache):
      return cache

    def comando(self,s):
        com = s.recv(1024)
        tempComando = com.split(' ')
        cmd=tempComando[0]
        key = tempComando[1]
        value = tempComando[2]

        if cmd == 'set':
            res = self.setDict(key,value)
            s.send(res)
        elif cmd == 'get':
            res = self.getDictValue(key)
            s.send(res)