import time
import threading
from multiprocessing.dummy import Pool as ThreadPool

def squareNumber(n):
	return n**2

def calculateParallel(numbers, threads=2):
	pool = ThreadPool(threads)
	results = pool.map(squareNumber, numbers)
	pool.close()
	pool.join()
	return results


if __name__ == "__main__":
	numbers = [1,2,3,4,5]
	squaredNumbers = calculateParallel(numbers, 4)

	for n in squaredNumbers:
		print(n)


clients_list = ()
threads = list()

def imprimir_mensaje(mensaje):
	while True:
		print(mensaje)
		time.sleep(1)

# def main():
# 	mensaje = "Thread 1" #Variable aux
# 	mensaje2 = "Thread 2" #Variable aux
# 	#Empiezo el thread
# 	thread.start_new_thread(imprimir_mensaje, (mensaje,))
# 	thread.start_new_thread(imprimir_mensaje,(mensaje2,))
# 	x = raw_input("Estoy esperando que presione Enter...")
# 	print("Termino la funcion main")

# main()
