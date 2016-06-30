import threading
from time import sleep

class MainThread(threading.Thread):
	cache = None # variable de clase
	def __init__(self):
		threading.Thread.__init__(self)
		self.clientSocket = None #variable de instancia
		

	def run(self):
		if self.clientSocket is not None
			print "aqui va un receive y tons of code"
		else:
			sleep(0)
		
