from tabuleiro import Tabuleiro
from random import randint
from copy import deepcopy


## Gera um tabuleiro em que so tem 1 rainha por coluna
## Retorna uma instância de Tabuleiro
def gerarTabuleiro():
	tabuleiro = Tabuleiro()
	tabuleiro.tabuleiro = [['_' for x in range(8)] for x in range(8)]

	for coluna in range(8):
		linha = randint(0,7)

		tabuleiro.tabuleiro[linha][coluna] = "Q"

	tabuleiro.custo = calculaColisoes(tabuleiro.tabuleiro)

	return tabuleiro

def calculaColisoes(tabuleiro):
	qtdColisoesLC = 0
	qtdColisoesD = 0
	for x in range(8):
		for y in range(8):
			if tabuleiro[x][y] == "Q":

				""" COLISOES NA LINHA E COLUNA"""
				for k in range(8):
					if tabuleiro[x][k] == "Q":
						qtdColisoesLC+=1
					if tabuleiro[k][y] == "Q":
						qtdColisoesLC +=1

				# Subtrai aqui, pois as colisoes = qtdRainhasLinha + qtdRainhasColuna- 2
				qtdColisoesLC-=2

				""" COLISOES NA DIAGONAL """

				# Colisoes diagonal Inferior Esquerda
				i, j = x+1, y-1
				while (i < 8 and  j>=0):
					if tabuleiro[i][j] == "Q":
						qtdColisoesD += 1

					i+=1
					j-=1

				# Colisoes diagonal Inferior Direita 
				i, j = x+1, y+1
				while (i<8 and j < 8):
					if tabuleiro[i][j] == "Q":
						qtdColisoesD += 1

					i+=1
					j+=1

				# Colisoes diagonal Superior Esquerda
				i, j = x-1, y-1
				while (i>=0 and j>=0):
					if tabuleiro[i][j] == "Q":
						qtdColisoesD += 1

					i-=1
					j-=1

				# Colisoes diagonal Superior Direita
				i, j = x-1, y+1
				while (i>=0 and j<8):
					if tabuleiro[i][j] == "Q":
						qtdColisoesD += 1

					i-=1
					j+=1 



	return (qtdColisoesLC + qtdColisoesD)/2


def printarTabuleiro(tabuleiro):
	for x in range(8):
		for y in range(8):
			print (tabuleiro[x][y], end="  ")

		print ("\n")