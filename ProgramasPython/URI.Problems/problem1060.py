## 
## Numeros Positivos
## URI ONLINE - Problema 1060 - Iniciante
##
## Created by Jon on 16.03.2016
##	

# -*- coding: utf-8 -*-

cont = 0

for x in range(1,7):
	valor = input()
	if valor>0:
		cont+=1
		
print ("%d valores positivos"%(cont))
