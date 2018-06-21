## 
## Pares entre Cinco Numeros
## URI ONLINE - Problema 1065 - Iniciante
##
## Created by Jon on 16.03.2016
##	

# -*- coding: utf-8 -*-

cont = 0

for x in range(1,6):
	valor = input()
	if not(valor%2):
		cont+=1
		
print ("%d valores pares"%(cont))
