############################################
## Soma de Impares Consecutivos I
## URI ONLINE - Problema 1071 - Iniciante
##
## Created by Jon on 21.03.2016
##	

# -*- coding: utf-8 -*-

cont_Impar = 0

valor1 = input()
valor2 = input()

if valor1>valor2:
	valor1 = valor1^valor2
	valor2 = valor1^valor2
	valor1 = valor1^valor2
	
for x in range(valor1+1, valor2):
	if x%2:
		cont_Impar += x
		
print (cont_Impar)