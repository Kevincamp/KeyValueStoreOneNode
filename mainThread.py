import threading

class MainThread(threading.Thread):
	def __init__(self, num):
		threading.Thread.__init__(self)
		self.num = num
	def run(self):
		print "Soy el hilo", self.num

for i in range(0,10):
	t = MainThread(i)
	t.start()
	t.join()
	print "Fin."