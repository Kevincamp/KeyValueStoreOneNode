import threading
from time import sleep

class MainThread(threading.Thread):
	def __init__(self, command):
		threading.Thread.__init__(self)
		self.command = command

	def run(self):
		if self.command != "":
			print "El comando es: " + self.command
		else:
			sleep(5)
		
comandos = ["del -a","add b", ""]
for comando in comandos:
	t = MainThread(comando)
	t.start()
	t.join()
	print "Fin"