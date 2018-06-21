############################################
## Sequencia IJ 4
## URI ONLINE - Problema 1098 - Iniciante
##
## Created by Jon on 21.03.2016
##	

# -*- coding: utf-8 -*-

"""
CODIGO ANTIGO: NAO FUNCIONA

valor = 0
while valor <=2:
        for x in range(1,4): 
		if valor == 0 or valor == 1 or valor ==2:  
			print ("I=%d J=%d"%(valor,valor+x))
		
		else:
			print ("I=%.1f J=%.1f"%(valor,valor+x))
	valor+=0.2



"""

kappa = 0

while kappa < 22:   ## O computador nao consegue representar o numero 0.2, por isso tive que somar de 2 em 2, e dividir por 10.0 para obter os resultados que queria.
	for x in range(1,4):
		valor = kappa/10.0 
		if valor==0 or valor==1 or valor==2:
			print ("I=%d J=%d"%(valor,valor+x))
		
		else:
			print ("I=%.1f J=%.1f"%(valor,valor+x))
	kappa+=2
