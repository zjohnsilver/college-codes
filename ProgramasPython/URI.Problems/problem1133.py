############################################
## Resto da Divisao
## URI ONLINE - Problema 1133 - Iniciante
##
## Created by Jon on 24.03.2016
##	

# -*- coding: utf-8 -*-

#Recebendo os valores X e Y
X = input()
Y = input()

if X>Y:  # Inverter os valores para que o X seja sempre o inicio do laco for
	aux = X
	X = Y
	Y = aux

#Laco que vai de X a Y e printa os valores que % 5 == 2 or %5 == 3
for x in range(X+1,Y):
	if x%5==2 or x%5==3:
		print ("%d"%(x))


	
