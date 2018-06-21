## 
## Quadrado de Pares
## URI ONLINE - Problema 1073 - Iniciante
##
## Created by Jon on 16.03.2016
##	

# -*- coding: utf-8 -*-

n = input()

for x in range(1,n+1):
	if not(x%2):
		print ("%d^2 = %d"%(x,x**2))
		

