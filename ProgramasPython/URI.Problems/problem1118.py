############################################
## Varias Notas Com Validacao
## URI ONLINE - Problema 1118 - Iniciante
##
## Created by Jon on 23.03.2016
##	

# -*- coding: utf-8 -*-

codigo = 1

while codigo==1:
	soma = 0 
	for x in range(1,3):
		nota = input()

		while nota<0 or nota>10:
			print "nota invalida"
			nota = input()

	
		soma += nota

	print ("media = %.2f"%(soma/2.0))
	
	print ("novo calculo (1-sim 2-nao)")
	codigo = input()

	while codigo!=1 and codigo!=2:
		print ("novo calculo (1-sim 2-nao)")
		codigo = input()
