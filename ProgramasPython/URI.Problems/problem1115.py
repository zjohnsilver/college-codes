############################################
## Quadrante
## URI ONLINE - Problema 1115 - Iniciante
##
## Created by Jon on 23.03.2016
##	

# -*- coding: utf-8 -*-

continuar = 1

while continuar:
	string = raw_input().split()

	X = int(string[0])
	Y = int(string[1])


	if X!=0 and Y!=0:
		if X>0 and Y>0:
			print ("primeiro")

		elif X<0 and Y>0:
			print ("segundo")
		
		elif X<0 and Y<0:
			print ("terceiro")
		
		else:
			print ("quarto")

	else:
		continuar = 0
		



