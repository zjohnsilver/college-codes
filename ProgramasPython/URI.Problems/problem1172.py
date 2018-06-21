############################################
## Substituição em Vetor I
## URI ONLINE - Problema 1172 - Iniciante
##
## Created by Jon in 19.06.2016
##	
## Python 3

lista = [ ]

for x in range(10):
	lista.append(int(input()))
	if lista[x] <=0:
		lista[x] = 1

	print ("X[%d] = %d" %(x, lista[x]))
