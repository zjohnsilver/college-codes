############################################
## Sequencia de Numeros e Soma
## URI ONLINE - Problema 1101 - Iniciante
##
## Created by Jon on 23.03.2016
##	

# -*- coding: utf-8 -*-

continuar = 1

while continuar:
	string = ''
	string2= ' '
	soma = 0
	
	entrada = raw_input().split()
	
	M = int(entrada[0])
	N = int(entrada[1])
	
	if M>0 and N>0:
		if M>N:
			aux = M
			M = N
			N = aux
	
		for x in range(M, N+1):
			string = string + str(x) + string2
			soma+=x

		print ("%sSum=%d"%(string, soma))

	else:
		continuar = 0

	 

