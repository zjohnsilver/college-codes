############################################
## Validacao de Nota
## URI ONLINE - Problema 1117 - Iniciante
##
## Created by Jon on 23.03.2016
##	

# -*- coding: utf-8 -*-

soma = 0 

for x in range(1,3):
	nota = input()

	while nota<0 or nota>10:
		print "nota invalida"
		nota = input()

	
	soma += nota

print ("media = %.2f"%(soma/2.0))




	
