## 
## Positivos e Media
## URI ONLINE - Problema 1064 - Iniciante
##
## Created by Jon on 16.03.2016
##	

# -*- coding: utf-8 -*-

cont = 0
cont2 = 0

for x in range(1,7):
	valor = input()
	if valor>0:
		cont+=1
		cont2+=valor
		
print ("%d valores positivos"%(cont))
print ("%.1f"%(cont2/cont))
