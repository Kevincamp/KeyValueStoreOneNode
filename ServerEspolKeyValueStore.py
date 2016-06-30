#!/usr/bin/python
# coding=utf-8                   #This is server.py file

import socket                   #Import socket module
from multiprocessing.dummy import Pool as ThreadPool #Import tread pool
import mainThread

#Globals (Start with capital letter)
Pool = []

def aTrabajarHilos(socket):  #Verifica cada hilo, si el hilo que esta escuchando no tiene socket y lo pone a trabajar(se lo pasa)
    pass
def inicializarHilos(numeroHilos):
    for i in range(numeroHilos):
        thread = mainThread()
        thread.start()
        Pool.append(thread)
    createDictionary()
    pass


def createDictionary():
    dictionary = dict([(clientSocket,),(threadClient,)])

s = socket.socket()               #Se crea el objeto socket
host = socket.gethostname()     #Se obtiene el hostname de la máquina
port = 12345
s.bind(('',port))             #Bind to the port
s.settimeout(10)
s.listen(5)
queue = []
cache = {}
inicializarHilos(5); 
print Pool
while True:
    try:
        c,addr = s.accept()
        queue.append(c)
    except socket.timeout:
        continue
    if len(queue) > 0:
        clientSocket = queue.pop(0)
        aTrabajarHilos()



