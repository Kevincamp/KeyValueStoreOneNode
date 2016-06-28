#!/usr/bin/python
# coding=utf-8                   #This is server.py file

import socket                   #Import socket module

s=socket.socket()               #Se crea el objeto socket
host = socket.gethostname()     #Se obtiene el hostname de la máquina
port = 12345
s.bind((host,port))             #Bind to the port
s.settimeout(None)
s.listen(5)                     # Espera por la conexión del cliente. Numero de clientes que puede aceptar
c,addr = s.accept()

while True:
    # Se establece la conexión con el cliente
    print 'Conexión de:', addr
    entranc = c.recv(1024)
    tempCKV = entranc.split(' ')
    command = tempCKV[0]
    key = tempCKV[1]
    value = tempCKV [2]

    if command == "exit":
        c.close()
    elif command == "list":
        c.send('Me llego este comando:'+ command)
        entranc=" "
    else:
        c.send('Me llego este comando:' + command +' ' + key+ ' ' + value)
        entranc = " "

