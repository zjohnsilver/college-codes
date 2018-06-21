############################################
## Sequencia Logica
## URI ONLINE - Problema 1144 - Iniciante
##
## Created by Jon on 24.03.2016
##	

# -*- coding: utf-8 -*-

N = input()

for x in range(1, N+1):
	for y in range(0,2):
		string = str(x) + " " + str(x**2 + y) + " " + str(x**3 + y)
		print ("%s"%(string)) 
