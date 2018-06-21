############################################
## PUM
## URI ONLINE - Problema 1142 - Iniciante
##
## Created by Jon on 24.03.2016
##	

# -*- coding: utf-8 -*-

# Entrada: 7
# Saida:
"""
		1 2 3 PUM
		5 6 7 PUM
		9 10 11 PUM
		13 14 15 PUM
		17 18 19 PUM
		21 22 23 PUM
		25 26 27 PUM
"""

N = input()
string = ''
string2 = ' '

for x in range(1, ((N*3) + (N-1))+2): #Laco necessario para a sequencia..
	if x%4:
		string = string + str(x) + string2
	
	if not(x%4):
		string+="PUM"
		print ("%s"%(string))
		string = ''
		string2 = ' '
	
