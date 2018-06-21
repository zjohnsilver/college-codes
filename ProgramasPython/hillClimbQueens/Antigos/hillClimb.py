from noRainha import noRainha
from random import randint
from copy import deepcopy


def gerarPonto():
	return (randint(0,7), randint(0,7)) 

def gerarTabuleiro():
	tabuleiro = [[noRainha() for x in range(8)] for x in range(8)]

	for i in range(8):
		x, y = gerarPonto()

		while (tabuleiro[x][y].estado == "Q"):
			x, y = gerarPonto()

		tabuleiro[x][y].estado = "Q"


	return tabuleiro


def printarTabuleiro(tabuleiro):
	for x in range(8):
		for y in range(8):
			print (tabuleiro[x][y].estado, end=" ")

		print ()


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



def limite (linha, coluna):
	dimensao = 8
	return (linha<dimensao and linha>=0) and (coluna<dimensao and coluna>=0) 


def moverUmaRainha(tabuleiro):
	newTabuleiro = deepcopy(tabuleiro)
	# Andar nos valores ao redor
	dLinha = [-1, -1, -1, 0, 0, 1, 1, 1]
	dColuna = [-1, 0, 1, -1, 1, -1, 0, 1]

	x, y = gerarPonto()

	# Gera um novo ponto, até que encontre uma rainha
	while (newTabuleiro[x][y].estado != "Q"):
		x, y = gerarPonto()

	xInicial, yInicial = x, y

	k = 0
	for i in range(8):
		x, y = x + dLinha[k], y + dColuna[k]

		if limite(x, y) and tabuleiro[x][y] != "Q":
			newTabuleiro[xInicial][yInicial].estado = "_"
			newTabuleiro[x][y].estado = "Q"

			return newTabuleiro

	return newTabuleiro

"""
tabuleiro = gerarTabuleiro()

printarTabuleiro(tabuleiro)

print()

tabuleiro2 = moverUmaRainha(tabuleiro)

printarTabuleiro(tabuleiro)
"""


def hillClimb():
	colisoesLimite = 100
	melhorTabuleiroPossivel = ""
	execucoesGerandoTabuleiro = 100
	y = 0
	while (y < execucoesGerandoTabuleiro):
		execucoesHillClimbing = 100
		tabuleiro = gerarTabuleiro()

		x = 0
		while (x < execucoesHillClimbing):
			colisoes = calculaColisoes(tabuleiro)

			vizinho = moverUmaRainha(tabuleiro)
			colisoesVizinho = calculaColisoes(vizinho)

			if colisoesLimite > colisoes:
				melhorTabuleiroPossivel = deepcopy(tabuleiro)
				colisoesLimite = colisoes

			if colisoesVizinho >= colisoes and (colisoes <1):
				return tabuleiro

			tabuleiro = deepcopy(vizinho)

			x+=1
		print (colisoesLimite)

		y+=1
	return melhorTabuleiroPossivel

solucao = hillClimb()

printarTabuleiro(solucao)

print (calculaColisoes(solucao))


"""
tabuleiro = gerarTabuleiro()
colisoes = calculaColisoes(tabuleiro)

while (colisoes > 2):
	tabuleiro = gerarTabuleiro()
	colisoes = calculaColisoes(tabuleiro)


printarTabuleiro(tabuleiro)
print (colisoes)
"""