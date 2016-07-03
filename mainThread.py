# coding=utf-8
import threading
from threading import Lock
from time import sleep
import socket
import re
class MainThread(threading.Thread):
	cache = {} # variable de clase
	candado = Lock()
	def __init__(self):
		threading.Thread.__init__(self)
		self.clientSocket = None #variable de instancia

	def run(self):
		while True:
			if self.clientSocket is not None:
				self.comando(self.clientSocket)
			else:
				sleep(1)

	def setClientSocket(self,s):
		self.clientSocket = s
		self.clientSocket.settimeout(5)
		try:
			self.clientSocket.send("ok")
			self.clientSocket.settimeout(None)
		except socket.timeout:
			self.clientSocket.close()
			self.clientSocket = None	
		

	def getClientSocket(self):
		return self.clientSocket

	#Funcion que ejecuta el comando "set"
	def setDict(self,key,value): #SET
		self.candado.acquire()
		if key in self.cache:
			self.cache[key] = value
		else:
			self.cache[key] = value
		res = 'OK'
		self.candado.release()
		return res

	#Funcion que ejecuta el comando "del"
	def delDict(self,key): #DEL
		self.candado.acquire()
		if key in self.cache:
			del self.cache[key]
			res='Elemento eliminado'
		else:
			res='ERROR: No existe un valor asociado a esa clave en el diccionario'
		self.candado.release()
		return res


	def getDictValue(self,key): #GET
		res = "key = "
		self.candado.acquire()
		for clave in self.cache.keys():
			if key == clave:
				res = res + str(self.cache[clave])
				break
		self.candado.release()
		return res

	def getDict(self): #LIST
		res = ""
		self.candado.acquire()
		for clave in self.cache.keys():
			res += clave + "\n"
		self.candado.release()
		return res + " "

	def comando(self,s):
		com = s.recv(4096)
		regex = "^(\S+)[ \t\r]*(\S*)[ \t\r]*([ \t\r\S]*)$"
		patron = re.compile(regex)
		tempComando = patron.match(com)
		cmd = str(tempComando.group(1)).lower()
		key = str(tempComando.group(2))
		value = str(tempComando.group(3))

		if cmd == 'set':
			res = self.setDict(key,value)
			s.send(res)
		elif cmd == 'get':
			res = self.getDictValue(key)
			s.send(res)
		elif cmd == 'list':
			res = self.getDict()
			s.send(res)
		elif cmd =='del':
			res=self.delDict(key)
			s.send(res)
		elif cmd =='exit':
			self.clientSocket.close()
			self.clientSocket = None
		else:
			s.send('ERROR: Instrucción no reconocida por el servidor')