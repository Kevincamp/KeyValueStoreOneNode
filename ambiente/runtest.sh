#!/bin/bash
clear
date
echo "TESTING WORKLOAD"
operacion="lectura"
workload="read.txt"
db="espol"
host="espol.host=127.0.0.1"
port="espol.port=12345"
for i in 1 2 3 4 5
do
	for j in 1 2 3 4 5
	do
		pkill python
		python ./propio/ServerEspolKeyValueStore.py &
		./bin/ycsb load $db -s -P workloads/$workload -p "$host" -p "$port" -threads $i > ./pruebas/$operacion$i$j.txt
		./bin/ycsb run $db -s -P workloads/$workload -p "$host" -p "$port" -threads $i> ./pruebas/$operacion$i$j.txt
		pkill python
		echo "Terminado test hilo: " $i "iteracion: " $j
	done
done