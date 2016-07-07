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
		try:	# Si aun se encuentra esperando se lo atiende
			self.clientSocket.send("ok")
			self.clientSocket.settimeout(None)
		except socket.timeout: # caso contrario se lo descarta
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
		tamMsg = s.recv(10) # se recibe el tamaño de la cadena
		try:
			com = self.listenClient(int(tamMsg))
		except ValueError:
			s.send('ERROR: Problema en el protocolo de comunicación')
			return	
		regex = "^(\S+)[ \t\r]*(\S*)[ \t\r]*([ \t\r\S]*)$"
		patron = re.compile(regex)
		tempComando = patron.match(com)
		cmd = str(tempComando.group(1)).lower()
		key = str(tempComando.group(2))
		value = str(tempComando.group(3))
		s.settimeout(600) # valido si el cliente sigue activo
		try:
			if cmd == 'set':
				try:
					res = self.setDict(key,value)
				except MemoryError:
					res="ERROR: El diccionario se quedo sin memoria. Use el comando 'del' para liberarla"
				s.send(res)
				s.settimeout(None) 
			elif cmd == 'get':
				res = self.getDictValue(key)
				self.notifyClient(res)
				s.settimeout(None) 
			elif cmd == 'list':
				res = self.getDict()
				self.notifyClient(res)
				s.settimeout(None) 
			elif cmd =='del':
				res=self.delDict(key)
				s.send(res)
				s.settimeout(None) 
			elif cmd =='exit':
				self.clientSocket.close()
				self.clientSocket = None
			else:
				s.send('ERROR: Instrucción no reconocida por el servidor')
		except socket.timeout:
			self.clientSocket.close()
			self.clientSocket = None
		# el socket vuelve a blocking state para esperar una peticion del cliente

	def listenClient(self, tam):
		cadena = ""
		sample = 1024 * 100
		it = tam / sample
		if tam < sample:
			return self.clientSocket.recv(tam)
		if it*sample < tam:
			it = it + 1
		#print "iteraciones: " , it
		while(it > 0):
			if it == 1:
				cadena = cadena + self.clientSocket.recv(tam)
			else:
				cadena = cadena + self.clientSocket.recv(sample)
			it = it - 1
		return cadena

	def notifyClient(self,cadena):
		longitud = len(cadena.encode('utf-8'))
		#separador $operativos$ -> 12 BYTES
		sample = 1012
		if longitud <= 1024:
		 	self.clientSocket.send(cadena)
		 	return
		init = 0
		while init < longitud:
			chunk = cadena[init : init + sample]
			init = init + sample
			if init < longitud:
				chunk = chunk + "$operativos$"
			self.clientSocket.send(chunk)
