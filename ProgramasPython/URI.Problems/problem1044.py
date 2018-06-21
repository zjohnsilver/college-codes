## 
## Mostrar se os valores A e B sao multiplos ou nao
## URI ONLINE - Problema 1044 - Iniciante
##
## Created by Jon on 14.03.2016
##

# -*- coding: utf-8 -*-

string = raw_input().split()

A = int(string[0])
B = int(string[1])

if A==0 or B==0:
	print ("Sao Multiplos")

elif A==B or A%B==0 or B%A==0:
	print ("Sao Multiplos")

else:
	print ("Nao sao Multiplos")