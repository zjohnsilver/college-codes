## 
## Tempo de Jogo
## URI ONLINE - Problema 1046 - Iniciante
##
## Created by Jon on 15.03.2016
##	

# -*- coding: utf-8 -*-

string = raw_input().split()

hIni = int(string[0])
hFim = int(string[1])

duracao = -(hIni-24) + hFim  ## Essa formula e baseada na observacao de que hIni = 16 e hFim = 2, entao a duracao e de 10h.

if duracao>24:
	print ("O JOGO DUROU %d HORA(S)"%(duracao-24))
else:
	print ("O JOGO DUROU %d HORA(S)"%(duracao))
	
