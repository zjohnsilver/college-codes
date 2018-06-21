############################################
## Soma de Impares Consecutivos II
## URI ONLINE - Problema 1099 - Iniciante
##
## Created by Jon on 22.03.2016
##	

# -*- coding: utf-8 -*-

qtd = input("Quantidade: ")

for x in range(1, qtd+1):

	soma_Impares = 0

	string = raw_input("Valores: ").split()
	
	X = int(string[0])
	Y = int(string[1])
	
	if Y<X:
		Y = Y^X
		X = Y^X
		Y = Y^X
	
	for i in range(X+1, Y): ## Percorrendo os valores entre X e Y ou (X,Y)
		if i%2:
			soma_Impares += i
	
	print ("%d"%(soma_Impares))