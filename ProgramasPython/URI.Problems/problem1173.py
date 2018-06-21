############################################
## Preenchimento de Vetor I
## URI ONLINE - Problema 1173 - Iniciante
##
## Created by Jon in 19.06.2016
##	
## Python 3

entrada = int(input())
vetor = [ ]

for x in range(10):
	vetor.append(entrada)
	print ("N[%d] = %d" %(x, vetor[x]))
	entrada *= 2