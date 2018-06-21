############################################
## Quadrado e ao cubo
## URI ONLINE - Problema 1143 - Iniciante
##
## Created by Jon on 24.03.2016
##	

# -*- coding: utf-8 -*-

N = input()

for x in range(1, N+1):
	string = str(x) + " " + str(x**2) + " " + str(x**3)

	print ("%s"%(string)) 
	
