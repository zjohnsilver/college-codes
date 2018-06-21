############################################
## Grenais
## URI ONLINE - Problema 1131 - Iniciante
##
## Created by Jon on 24.03.2016
##	

# -*- coding: utf-8 -*-

continuar = 1

#Empate ou vitorias Inter ou vitorias Gremio
empate = 0
inter = 0
gremio = 0
total = 0

while continuar:
	string = raw_input().split()

	gol_Inter = int(string[0])
	gol_Gremio = int(string[1])

	if gol_Inter>gol_Gremio:
		inter += 1

	elif gol_Inter<gol_Gremio:
		gremio += 1

	else:
		empate += 1

	print ("Novo grenal (1-sim 2-nao)") # Deseja por mais um placar?
	
	grenal = input()

	if grenal != 1:
		continuar = 0
	
	total += 1

# Saida do programa, com estatisticas
print ("%d grenais"%(total))
print ("Inter:%d"%(inter))
print ("Gremio:%d"%(gremio))
print ("Empates:%d"%(empate))

if inter>gremio:
	print ("Inter venceu mais")

elif gremio>inter:
	print ("Gremio venceu mais")

else:
	print ("Nao houve vencedor")	

