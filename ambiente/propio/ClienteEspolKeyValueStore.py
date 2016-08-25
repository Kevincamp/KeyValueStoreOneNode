#!/usr/bin/python2.7
# coding=utf-8
import sys
import re
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
	if len(sys.argv) != 3:
		print "ERROR: faltan o sobran argumentos; ej: <ip del servidor> <puerto>"
		sys.exit(0);
	host = sys.argv[1]
	port = int(sys.argv[2])  #12345
	exflag = True
	s.connect((host, port))
	print "Conectando..."
	if s.recv(8) == "ok":
		while exflag:
			exflag = requestInput();
	sys.exit(0)

def requestInput():
	try:
		entry = str(raw_input(">> "))
	except EOFError:
		print "ERROR: se termino el buffer de entrada"
	regex = "^(\S+)[ \t\r]*(\S*)[ \t\r]*([ \t\r\S]*)$"
	patron = re.compile(regex)
	m = patron.match(entry)
	if m is not None:
		instruccion = str(m.group(1)).lower()
		clave = str(m.group(2))
		valor = str(m.group(3))
		if len(clave.encode('utf-8')) > 134217728 or len(valor.encode('utf-8')) > 2147483648:  #validacion del tamaño de claves y valores
			print "ERROR: La clave o el valor exceden los limites de 128 mb y 2gb respectivamente"
			return True
		requestlenstr = getRequesStrLen(instruccion,clave,valor)
		s.send(requestlenstr) # se envia el tamaño de la cadena a enviar
		if instruccion == "exit" and clave == "" and valor == "":

			s.send("exit")
			s.close()
			print "Cerrando la conexión..."
			return False
		elif instruccion == "help" and clave == "" and valor == "":
			print "get key: Operación ​get. Retorna el valor asociado a dicha clave"
			print "set key value: Almacena (en memoria) la clave, con el valor asociado."
			print "del key: Elimina la clave, con su valor asociado."
			print "list: Retorna la lista de todas las claves almacenadas"
			print "exit: Cierra la conexión con el servidor y termina la ejecución del programa"
			print "help: Muestra la lista de los comandos soportados, incluyendo una breve explicación de los mismos"
		elif instruccion == "get" and clave != "" and valor == "":
			s.send(instruccion+' '+clave)
			print getResponseServer(s)
		elif instruccion == "del" and clave != "" and valor == "":
			s.send(instruccion+' '+clave)
			print s.recv(1024)
		elif instruccion == "set" and clave != "" and valor != "":
			s.send(instruccion+' '+clave+' '+valor)
			print s.recv(4096)
		elif instruccion == "list" and clave == "" and valor == "":
			s.send(instruccion)
			print getResponseServer(s)
		else:
			print "ERROR: la instrucción dada no es válida"

	else:
		print "ERROR: la instrucción dada no es válida"
	return True


def getRequesStrLen(instruccion,clave,valor):
	longitud = str(len(clave.encode('utf-8')) + len(valor.encode('utf-8')) + len(instruccion.encode('utf-8')) + 2)
	while len(longitud) < 10:
		longitud = "0" + longitud
	#print longitud
	return longitud


def getResponseServer(server):
	cadena = server.recv(1024)
	result = ""
	while cadena[-12:] == "$operativos$":
		result = result + cadena[:-12]
		cadena = server.recv(1024)
	return result + cadena

if __name__ == "__main__":
	main()
