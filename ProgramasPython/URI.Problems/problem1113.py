############################################
## Crescente e Decrescente
## URI ONLINE - Problema 1113 - Iniciante
##
## Created by Jon on 21.03.2016
##	

# -*- coding: utf-8 -*-


X = 1
Y = 0

while X!=Y:
	string = raw_input().split()
	X = int(string[0])
	Y = int(string[1])
	
	if X>Y:
		print ("Decrescente")
	elif X<Y:
		print ("Crescente")
	
	