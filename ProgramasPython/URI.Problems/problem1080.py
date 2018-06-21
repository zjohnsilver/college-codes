############################################
## Maior e Posicao
## URI ONLINE - Problema 1080 - Iniciante
##
## Created by Jon on 21.03.2016
##	

# -*- coding: utf-8 -*-


for x in range(1,101):
	n = input()
	if x==1:
		maior=n
		pos = 1
		
	if n>maior:
		maior = n
		pos = x
		
print ("%d"%(maior))
print ("%d"%(pos))
		
	