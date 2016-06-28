import time
import threading

clients_list = ()
threads = list()

def imprimir_mensaje(mensaje):
	while True:
		print(mensaje)
		time.sleep(1)

def main():
	mensaje = "Thread 1" #Variable aux
	mensaje2 = "Thread 2" #Variable aux
	#Empiezo el thread
	thread.start_new_thread(imprimir_mensaje, (mensaje,))
	thread.start_new_thread(imprimir_mensaje,(mensaje2,))
	x = raw_input("Estoy esperando que presione Enter...")
	print("Termino la funcion main")

main()