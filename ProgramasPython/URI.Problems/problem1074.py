############################################ 
## Par ou Impar
## URI ONLINE - Problema 1074 - Iniciante
##
## Created by Jon on 21.03.2016
##	

# -*- coding: utf-8 -*-

qtd = int(input())
string = ""

for x in range(1,qtd+1):
	valor = input()
	
	if valor==0:
		print ("NULL")
	else:
		if not(valor%2):
			string += "EVEN"
			
		if valor%2:
			string += "ODD"
			
		if valor>0:
			string += " POSITIVE"
			
		if valor<0:
			string += " NEGATIVE"
		
		print (string)
		string = ""
			
	

