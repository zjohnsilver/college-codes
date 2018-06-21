############################################
## Medias Ponderadas
## URI ONLINE - Problema 1079 - Iniciante
##
## Created by Jon on 21.03.2016
##	

# -*- coding: utf-8 -*-

N = input()

for x in range (1, N+1):
	string = raw_input().split()
	
	nota1 = float(string[0])
	nota2 = float(string[1])
	nota3 = float(string[2])
	
	media = (nota1*2 + nota2*3 + nota3*5)/10.0
	
	print ("%.1f"%(media))