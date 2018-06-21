############################################
## Sequencia Logica 2
## URI ONLINE - Problema 1145 - Iniciante
##
## Created by Jon on 24.03.2016
##	

# -*- coding: utf-8 -*-

valores = raw_input().split()
X = int(valores[0])
Y = int(valores[1])
string = ''
string2 = ' '

for x in range(1, Y+1): #Laco necessario para a sequencia..
	if x%X:
		print x,
	else:
		print x	
