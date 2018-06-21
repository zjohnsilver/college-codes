############################################ 
## Pares, Impares, Positivos e Negativos
## URI ONLINE - Problema 1066 - Iniciante
##
## Created by Jon on 21.03.2016
##	

# -*- coding: utf-8 -*-

cont_Par = 0
cont_Impar = 0
cont_Pos = 0
cont_Neg = 0


for x in range(1,6):
	valor = input()
	
	if valor>0:
		cont_Pos+=1
	if valor<0:
		cont_Neg+=1
	if valor%2:
		cont_Impar+=1
	if not(valor%2):
		cont_Par+=1
		
print ("%d valor(es) par(es)"%(cont_Par))
print ("%d valor(es) impar(es)"%(cont_Impar))
print ("%d valor(es) positivo(s)"%(cont_Pos))
print ("%d valor(es) negativo(s)"%(cont_Neg))