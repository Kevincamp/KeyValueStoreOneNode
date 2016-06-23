#!/usr/bin/python2.7
# coding=utf-8
import sys;
import re

def main():
	if len(sys.argv) != 3:
		print "ERROR: faltan o sobran argumentos; ej: <ip del servidor> <puerto>"
		sys.exit(0);
	ipserver = sys.argv[1]
	port = sys.argv[2]
	exflag = True
	while exflag:
		exflag = requestInput();
	sys.exit(0)
def requestInput():
	entry = str(raw_input(">> "))
	#regex = "^([a-zA-Z0-9ñÑ_\-\/\\\.@áéíóú'!¡¿?+*:;]+)[ \t\r\f\v]+(\S+)[ \t\r\f\v]+([ \t\r\f\va-zA-Z0-9ñÑ_\-\/\\\.@áéíóú'!¡¿?+*:;]+)$"
	regex = "^(\S+)[ \t\r]*(\S*)[ \t\r]*([ \t\r\S]*)$"
	patron = re.compile(regex)
	m = patron.match(entry)
	if m is not None:
		#print m.group(1)
		#print m.group(2)
		#print m.group(3)
		instruccion = str(m.group(1)).lower()
		clave = str(m.group(2))
		valor = str(m.group(3))
		#inslen = len(m.groups())
		#print inslen
		if instruccion == "exit" and clave == "" and valor == "":
			print "Cerrando la conexión...."
			return False
		elif instruccion == "help" and clave == "" and valor == "":
			print "get key: Operación ​get. Retorna el valor asociado a dicha clave"
			print "set key value: Almacena (en memoria) la clave, con el valor asociado."
			print "del key: Elimina la clave, con su valor asociado."
			print "list: Retorna la lista de todas las claves almacenadas"
			print "exit: Cierra la conexión con el servidor y termina la ejecución del programa"
			print "help: Muestra la lista de los comandos soportados, incluyendo una breve explicación de los mismos"
		elif instruccion == "get" and clave != "" and valor == "":
			pass;
		elif instruccion == "del" and clave != "" and valor == "":
			pass;
		elif instruccion == "set" and clave != "" and valor != "":
			pass
		elif instruccion == "list" and clave == "" and valor == "":
			pass
		else:
			print "ERROR: la instrucción dada no es válida"
	else:
		print "ERROR: la instrucción dada no es válida"
	return True

if __name__ == "__main__":
    main()