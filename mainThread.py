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
                sleep(60)
            else:
                #print "entro"
                sleep(1)

    def setClientSocket(self,s):
        self.clientSocket = s

    def getClientSocket(self):
        return self.clientSocket

    def setDict(self,key,value):
        res = ''
        if key in self.cache:
            self.cache=self.cache.update(self.cache)
        else:
            self.cache[self.key]=value
        self.res = 'OK'

        return res

    def comando(self,s):
        com = s.recv(1024)
        tempComando = com.split('')
        cmd=tempComando[0]
        key = tempComando[1]
        value = tempComando[2]

        if cmd=='set':
            #res = self.setDict(key,value)
            get.send('El comando q se envio' + cmd + key + value)


    # def getValue(self, key,cache):
    # 	res = ""
    # 	if key in cache:
    # 		res = cache[key]
    # 	else:
    # 		res = "none value"
    # 	return res
    #
    # def listCache(self,cache):
    # 	return cache
    #
    # def runCommand(self,s):
    # 	entrance = s.recv(1024)
    # 	tempCKV = self.entranc.split(' ')
    # 	command = tempCKV[0]
    # 	key = tempCKV[1]
    # 	value = tempCKV[2]
    #
    # 	if command == "get":
    # 		res = self.getValue(key)
    # 		s.send(res)
    # 	elif command == "list":
    # 		res = self.listCache()
    # 		s.send(res)
    # 	else:
    # 		s.send('Me llego este comando:' + command +' ' + key+ ' ' + value)