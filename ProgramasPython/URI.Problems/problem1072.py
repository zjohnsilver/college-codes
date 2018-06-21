############################################
## Intervalo 2
## URI ONLINE - Problema 1072 - Iniciante
##
## Created by Jon on 21.03.2016
##	

# -*- coding: utf-8 -*-

qtd = input()
cont_In = 0
cont_Out = 0

for x in range(1, qtd+1):
	valor = input()
	
	if 10<=valor<=20:
		cont_In += 1
	
	else:
		cont_Out += 1
		
print ("%d in"%(cont_In))
print ("%d out"%(cont_Out))