############################################ 
## Seis Numeros Impares
## URI ONLINE - Problema 1070 - Iniciante
##
## Created by Jon on 19.03.2016
##	

# -*- coding: utf-8 -*-

valor = input()
cont=0

while cont<6:
	if valor%2:
		print ("%d"%(valor))
		cont+=1
	valor+=1
	
	