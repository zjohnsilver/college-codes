############################################
## Dividindo X por Y
## URI ONLINE - Problema 1116 - Iniciante
##
## Created by Jon on 23.03.2016
##	

# -*- coding: utf-8 -*-

N = input() # Valor do Laco

for x in range(1,N+1):
	string = raw_input().split()

	X = int(string[0])
	Y = int(string[1])

	if Y==0:  # Nao e possivel realizar divisao por zero
		print ("divisao impossivel")

	else:
		div = X/float(Y)
		print ("%.1f"%(div)) # Um digito apos a virgula

