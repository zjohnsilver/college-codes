############################################
## Multiplos de 13
## URI ONLINE - Problema 1132 - Iniciante
##
## Created by Jon on 24.03.2016
##	

# -*- coding: utf-8 -*-

#Recebendo os valores X e Y
X = input()
Y = input()

soma = 0

if X>Y:  # Inverter os valores para que o X seja sempre o inicio do laco for
	aux = X
	X = Y
	Y = aux

#Laco que vai de X a Y e soma os nao multiplos de 13
for x in range(X,Y+1):
	if (x%13):
		soma+=x


print ("%d"%(soma))
	
