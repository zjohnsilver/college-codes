from noRainha import noRainha
from random import randint
from copy import deepcopy



## Gera um tabuleiro em que so tem 1 rainha por coluna
def gerarTabuleiro():
	tabuleiro = [[noRainha() for x in range(8)] for x in range(8)]

	for coluna in range(8):
		linha = randint(0,7)

		tabuleiro[linha][coluna].estado = "Q"

	return tabuleiro


def printarTabuleiro(tabuleiro):
	for x in range(8):
		for y in range(8):
			print (tabuleiro[x][y].estado, end="  ")

		print ("\n")


def calculaColisoes(tabuleiro):
	qtdColisoesLC = 0
	qtdColisoesD = 0
	for x in range(8):
		for y in range(8):
			if tabuleiro[x][y].estado == "Q":

				""" COLISOES NA LINHA E COLUNA"""
				for k in range(8):
					if tabuleiro[x][k].estado == "Q":
						qtdColisoesLC+=1
					if tabuleiro[k][y].estado == "Q":
						qtdColisoesLC +=1

				# Subtrai aqui, pois as colisoes = qtdRainhasLinha + qtdRainhasColuna- 2
				qtdColisoesLC-=2

				""" COLISOES NA DIAGONAL """

				# Colisoes diagonal Inferior Esquerda
				i, j = x+1, y-1
				while (i < 8 and  j>=0):
					if tabuleiro[i][j].estado == "Q":
						qtdColisoesD += 1

					i+=1
					j-=1

				# Colisoes diagonal Inferior Direita 
				i, j = x+1, y+1
				while (i<8 and j < 8):
					if tabuleiro[i][j].estado == "Q":
						qtdColisoesD += 1

					i+=1
					j+=1

				# Colisoes diagonal Superior Esquerda
				i, j = x-1, y-1
				while (i>=0 and j>=0):
					if tabuleiro[i][j].estado == "Q":
						qtdColisoesD += 1

					i-=1
					j-=1

				# Colisoes diagonal Superior Direita
				i, j = x-1, y+1
				while (i>=0 and j<8):
					if tabuleiro[i][j].estado == "Q":
						qtdColisoesD += 1

					i-=1
					j+=1 



	return (qtdColisoesLC + qtdColisoesD)/2


def moverUmaRainha(tabuleiro):
    colisoes = calculaColisoes(tabuleiro)
    melhorTabuleiro = deepcopy(tabuleiro)
    #move one queen at a time, the optimal single move by brute force
    for ql in range(0,8):
    	for qc in range(0,8):
    		if tabuleiro[ql][qc].estado == "Q":
    			#get the lowest cost by moving this queen
	    		for ml in range(0,8):
	    			for mc in range(0,8):
	    				if tabuleiro[ml][mc].estado != "Q":
	    					#try placing the queen here and see if it's any better
	    					tentativa = deepcopy(tabuleiro)
	    					tentativa[ql][qc].estado = '_'
	    					tentativa[ml][mc].estado = "Q"
	    					colisoesTentativa = calculaColisoes(tentativa)
	    					if colisoesTentativa < colisoes:
	    						colisoes = colisoesTentativa
	    						melhorTabuleiro = tentativa
    
    return melhorTabuleiro


def hillClimb():
	tabuleiro = gerarTabuleiro()

	colisoesIguais = 0
	while (1):
		colisoes = calculaColisoes(tabuleiro)

		vizinho = moverUmaRainha(tabuleiro)
		colisoesVizinho = calculaColisoes(vizinho)

		if colisoesVizinho >= colisoes:
			return tabuleiro

		tabuleiro = deepcopy(vizinho)


TOTAL_EXECUCOES = 10
colisoes_exec = {}

i = 0
while (TOTAL_EXECUCOES>i):
	print ("Execução: %d" %(i))

	solucao = hillClimb()
	colisoes = calculaColisoes(solucao)

	if (i==0):
		melhor_solucao = Tabuleiro()


	if (str(colisoes) in colisoes_exec):
		colisoes_exec[str(colisoes)] +=1
	else:
		colisoes_exec[str(colisoes)] = 1

	TOTAL_EXECUCOES -= 1


for i in colisoes_exec.keys():
	print ("Colisoes de " + i + ": " + str((colisoes_exec[i]*100)/10.0) + "%")



TOTAL_EXECUCOES = 100
precisao = {}

i = 0
while (TOTAL_EXECUCOES>i):
	print ("%i "%(i))
	solucao = simulatedAnnealing()
	custo = solucao.custo

	## Se for a primeira execução ele armazena o primeiro custo, para testar com os próximos
	if (i==0):
		melhor_solucao = Tabuleiro()
		melhor_solucao.tabuleiro = deepcopy(solucao.tabuleiro)
		melhor_solucao.custo = solucao.custo 

	elif  custo < melhor_solucao.custo:
		melhor_solucao.tabuleiro = deepcopy(solucao.tabuleiro)
		melhor_solucao.custo = solucao.custo




	if (str(custo) in precisao):
		precisao[str(custo)] +=1
	else:
		precisao[str(custo)] = 1

	i+=1



print ("\n\nTabela de Precisão\n")

for i in precisao.keys():
	print ("Precisão de " + i + ": " + str((precisao[i]*100)/TOTAL_EXECUCOES) + "%")


