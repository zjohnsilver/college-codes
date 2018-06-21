from noRainha import noRainha
from random import randint, uniform
import math
from copy import deepcopy
import decimal


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


def simulatedAnnealing():
	temperatura = 4000
	sch = 0.99

	for i in range(0, 17):
		temperatura *= sch
		tabuleiro = gerarTabuleiro()
		vizinho = moverUmaRainha(tabuleiro)

		dw = calculaColisoes(vizinho) - calculaColisoes(tabuleiro)
		exp = .Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(-dw) * decimal.Decimal(temperatura)))

		if dw>0 or uniform(0,1) < exp:
			tabuleiro = deepcopy(vizinho)


		if calculaColisoes(tabuleiro) == 0:
			return tabuleiro

	print ("Não encontrou")
	return tabuleiro


TOTAL_EXECUCOES = 10
colisoes_exec = {}

while (TOTAL_EXECUCOES>0):
	print (TOTAL_EXECUCOES)
	solucao = simulatedAnnealing()
	colisoes = calculaColisoes(solucao)

	if (str(colisoes) in colisoes_exec):
		colisoes_exec[str(colisoes)] +=1
	else:
		colisoes_exec[str(colisoes)] = 1

	TOTAL_EXECUCOES -= 1


for i in colisoes_exec.keys():
	print ("Colisoes de " + i + ": " + str((colisoes_exec[i]*100)/10.0) + "%")
