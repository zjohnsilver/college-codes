############################################
## Sequencias Crescentes
## URI ONLINE - Problema 1146 - Iniciante
##
## Created by Jon on 24.03.2016
##	

# -*- coding: utf-8 -*-

X = 1

while X!=0:
	X = input()
	
	if X!=0:
		for y in range(1, X+1):
			if y != X:
				print y,
			else:
				print y
