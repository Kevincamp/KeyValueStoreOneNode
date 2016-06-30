#!/usr/bin/python
# coding=utf-8                   #This is server.py file

import socket                   #Import socket module

def aTrabajarHilos(socket):  #funcion que verifica si hay un hilo que no este escuchando ningun socket y lo pone a trabajar(se lo pasa)
    pass
def inicializarHilos(numeroHilos):
    pass

s = socket.socket()               #Se crea el objeto socket
host = socket.gethostname()     #Se obtiene el hostname de la máquina
port = 12345
s.bind(('',port))             #Bind to the port
s.settimeout(10)
s.listen(5)
queue = []
cache = {}
listaHilos=inicializarHilos(5); 
while True:
    try:
        c,addr = s.accept()
        queue.append(c)
    except socket.timeout:
        continue
    if len(queue) > 0:
        clientSocket = queue.pop(0)
        aTrabajarHilos()



