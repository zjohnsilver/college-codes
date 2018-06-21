############################################
## Número Perfeito
## URI ONLINE - Problema 1164 - Iniciante
##
## Created by Jon in 19.06.2016
##	
## Python 3

qtd_testes = int(input())

for x in range(qtd_testes):
	number = int(input())

	cont = 0

	for x in range(1, number):
		if (number % x == 0):
			cont += x

	if (cont == number):
		print ("%d eh perfeito" %(number))
	else:
		print ("%d nao eh perfeito" %(number))