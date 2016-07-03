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
	entry = str(raw_input(">> "))
	regex = "^(\S+)[ \t\r]*(\S*)[ \t\r]*([ \t\r\S]*)$"
	patron = re.compile(regex)
	m = patron.match(entry)
	if m is not None:
		instruccion = str(m.group(1)).lower()
		clave = str(m.group(2))
		valor = str(m.group(3))
		#inslen = len(m.groups())
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
			#s.send(instruccion+' '+clave+' '+' ')
			s.send(str(entry))
			print s.recv(4096)
		elif instruccion == "del" and clave != "" and valor == "":
			s.send(instruccion+' '+clave+' '+valor)
			print s.recv(1024)
		elif instruccion == "set" and clave != "" and valor != "":
			s.send(instruccion+' '+clave+' '+valor)
			print s.recv(4096)
		elif instruccion == "list" and clave == "" and valor == "":
			s.send(entry)
			print s.recv(4096)
		else:
			print "ERROR: la instrucción dada no es válida"

	else:
		print "ERROR: la instrucción dada no es válida"
	return True

if __name__ == "__main__":
	main()
