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
