############################################
## Tempo de Jogo com minutos
## URI ONLINE - Problema 1047 - Iniciante
##
## Created by Jon on 15.03.2016
##	

# -*- coding: utf-8 -*-

string = raw_input().split()

hIni = int(string[0])
minIni = int(string[1])
hFim = int(string[2])
minFim = int(string[3])

duraHoras = hFim-hIni  ## Essa formula e baseada na observacao de que hIni = 16 e hFim = 2, entao a duracao e de 10h.
duraMin = minFim-minIni ## Essa formula e baseada na observacao de que minIni = 10 e minFim = 5, entao a duracao e de 55min

if hIni==hFim==minIni==minFim:
	duraHoras+=24

else:
	if duraMin<0:
		duraMin+=60
		duraHoras-=1
	
	if duraHoras<0:
		duraHoras+=24
	

print ("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(duraHoras, duraMin))
