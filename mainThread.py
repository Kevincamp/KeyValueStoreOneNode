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

    #Funcion que ejecuta el comando "set"
    def setDict(self,key,value):
        if key in self.cache:
            self.cache[key] = value
        else:
            self.cache[key] = value
        res = 'OK'
        return res

    #Funcion que ejecuta el comando "del"
    def delDict(self,key):
        if key in self.cache:
            del self.cache[key]
            res='Elemento eliminado'
        else:
            res='ERROR: No existe un valor asociado a esa clave en el diccionario'
        return res


    def getDictValue(self,key):
      res = ""
      for self.key in self.cache.keys():
        if key == self.key:
            res = self.cache[self.key]
        break
      return res

    def getDict(self):
        res = ""
        for self.key in self.cache.keys():
            res += self.key +"->"+self.cache[self.key]+"\n"
        return res

    def comando(self,s):
        com = s.recv(4096)
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
<<<<<<< HEAD
        elif cmd == 'list':
            res = self.getDict()
=======
        elif cmd=='del':
            res=self.delDict(key)
>>>>>>> 8917f9aaa0091a783579a8750e7e1db41a9b3a2a
            s.send(res)