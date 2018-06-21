############################################ 
## Tempo de um evento
## URI ONLINE - Problema 1061 - Iniciante
##
## Created by Jon on 18.03.2016
##	

# -*- coding: utf-8 -*-

string = raw_input().split()
string2 = raw_input().split()
string3 = raw_input().split()
string4 = raw_input().split()

diaIni = int(string[1])
hIni = int(string2[0])
minIni = int(string2[2])
segIni = int(string2[4])

diaFim = int(string3[1])
hFim = int(string4[0])
minFim = int(string4[2])
segFim = int(string4[4])

duraDias = diaFim - diaIni
duraHoras = hFim - hIni  ## Essa formula e baseada na observacao de que hIni = 16 e hFim = 2, entao a duracao e de 10h.
duraMin = minFim - minIni ## Essa formula e baseada na observacao de que minIni = 10 e minFim = 5, entao a duracao e de 55min
duraSeg = segFim - segIni
if duraSeg<0:
	duraSeg+=60
	duraMin-=1

if duraMin<0:
	duraMin+=60
	duraHoras-=1

if duraHoras<0:
	duraHoras+=24
	duraDias-=1
	



print ("%d dia(s)"%(duraDias))
print ("%d hora(s)"%(duraHoras))
print ("%d minuto(s)"%(duraMin))
print ("%d segundo(s)"%(duraSeg))


