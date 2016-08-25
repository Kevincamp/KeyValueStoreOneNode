#!/bin/bash
clear
date
echo "TESTING WORKLOAD"
operacion="lectura"
workload="read.txt"
db="espol"
host="espol.host=127.0.0.1"
port="espol.port=12345"
for i in 8 10
do
	for j in 1 2 3 4 5
	do
		pkill python
		python ./propio/ServerEspolKeyValueStore.py &
		./bin/ycsb load $db -s -P workloads/$workload -p "$host" -p "$port" -threads $i > ./pruebas/load$operacion$i$j.txt
		./bin/ycsb run $db -s -P workloads/$workload -p "$host" -p "$port" -threads $i> ./pruebas/run$operacion$i$j.txt
		pkill python
		echo "++++++++++EJECUCION TERMINADA EN HILO: " $i "ITERACION: " $j" ++++++++++++++"
	done
done