############################################
## Número Primo
## URI ONLINE - Problema 1165 - Iniciante
##
## Created by Jon in 19.06.2016
##	
## Python 3

qtd_testes = int(input())

for x in range(qtd_testes):
	number = int(input())

	cont = 0

	for x in range(1, number+1):
		if (number % x == 0):
			cont += 1

	if (cont == 2):
		print ("%d eh primo" %(number))
	else:
		print ("%d nao eh primo" %(number))