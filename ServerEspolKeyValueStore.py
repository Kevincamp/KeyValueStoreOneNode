#!/usr/bin/python
# coding=utf-8                   #This is server.py file

import socket                   #Import socket module
from mainThread import MainThread
import re
def loadWork(spool,socketclt):  #Verifica cada hilo, si el hilo que esta escuchando no tiene socket y lo pone a trabajar(se lo pasa)
	for index,the_thread in enumerate(spool):
		if the_thread.getClientSocket() is None:
			the_thread.setClientSocket(socketclt)
			return True
	return False

# inicializa los hilos y los mete un pool(lista)
def initThreads(pool,threadNumber):
	for i in range(threadNumber):
		thread = MainThread()
		thread.start()
		pool.append(thread)

s = socket.socket()               #Se crea el objeto socket
host = socket.gethostname()     #Se obtiene el hostname de la máquina
port = 12345
s.bind(('',port))             #Bind to the port
s.settimeout(5)
s.listen(5)
queue = []
pool = []
initThreads(pool,10);
while True:
	if len(queue) > 0: #verifico si existen clientes pendientes en la cola
		clientSocket = queue.pop(0)
		if not loadWork(pool,clientSocket): # si no se logra atender a un cliente
			queue.insert(0, clientSocket) # el cliente vuelve al inicio de la cola
			#print "Hay " , len(queue), " Clientes en la cola"
	try:
		c,addr = s.accept() # se recepta una conexion
		print 'Conexion establecida desde', addr
		queue.append(c) # se ingresa el socket a la cola de clientes por atender

	except socket.timeout:
		continue
