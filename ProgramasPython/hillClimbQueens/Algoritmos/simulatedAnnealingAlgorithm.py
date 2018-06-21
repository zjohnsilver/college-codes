from tabuleiro import Tabuleiro
from funcoes import *
from random import randint, uniform
from copy import deepcopy
import math

## Recebe uma instância da classe Tabuleiro
## Move uma rainha na coluna dela
def moverUmaRainha(tabuleiro):
	coluna = randint(0,7)

	linha = 0
	for x in range(0, 8):
		if tabuleiro.tabuleiro[x][coluna] == "Q":
			linha = x
			break

	# Se a rainha estiver na borda superior, ele deve ir para baixo
	if linha == 0:
		direcao = 1

	# Se a rainha estiver na borda inferior, ela deve ir para cima
	elif linha == 7:
		direcao = 0

	# Caso não esteja em nenhuma borda, ela por ir para cima/baixo
	else:
		direcao = randint(0,1)


	casa_para_andar = randint(1, 6)

	
	if direcao:
		while linha + casa_para_andar > 7:
			casa_para_andar = randint(1,6)

		nova_linha = linha + casa_para_andar

	else:
		while linha - casa_para_andar <0:
			casa_para_andar = randint(1,6)

		nova_linha = linha - casa_para_andar


	# Mudando a rainha de lugar
	tabuleiro.tabuleiro[linha][coluna] = "_"
	tabuleiro.tabuleiro[nova_linha][coluna] = "Q"

	## Recalcula o custo do tabuleiro, após mover a rainha
	tabuleiro.custo = calculaColisoes(tabuleiro.tabuleiro)


def simulatedAnnealing():
	Ti = 100
	Tf = 0.1
	taxa = 0.8

	S0 = gerarTabuleiro() #Solução Inicial
	S = S0 #(Solucao Atual)

	n_iteracoes = 50

	melhor_solucao = S0

	T = Ti
	while (T > Tf):
		for x in range(n_iteracoes):
			vizinho = Tabuleiro()
			vizinho.tabuleiro = deepcopy(S.tabuleiro)
			moverUmaRainha(vizinho)

			deltaCusto = vizinho.custo - S.custo

			if deltaCusto < 0:
				S = vizinho

			else:
				numero_random = uniform(0,1)

				## Aceita estados piores
				## A função exp diminue conforme T diminue
				if numero_random < math.exp(-deltaCusto/T):
					S = vizinho

			if (S.custo < melhor_solucao.custo):
				melhor_solucao = S


		T = taxa*T

	return melhor_solucao



TOTAL_EXECUCOES = int(input("\nTotal Execuções: "))
precisao = {}

i = 0
while (TOTAL_EXECUCOES>i):
	print ("\nTotalExecução: %i "%(i))
	solucao = simulatedAnnealing()
	custo = solucao.custo

	print ("\tCusto: %d" %(custo))

	## Se for a primeira execução ele armazena o primeiro custo, para testar com os próximos
	if (i==0):
		melhor_solucao = Tabuleiro()
		melhor_solucao.tabuleiro = deepcopy(solucao.tabuleiro)
		melhor_solucao.custo = custo 

	elif  custo < melhor_solucao.custo:
		melhor_solucao.tabuleiro = deepcopy(solucao.tabuleiro)
		melhor_solucao.custo = custo




	if (str(custo) in precisao):
		precisao[str(custo)] +=1
	else:
		precisao[str(custo)] = 1

	i+=1



print ("\n\nTabela de Precisão\n")

for i in precisao.keys():
	print ("Precisão de " + i + ": " + str((precisao[i]*100)/TOTAL_EXECUCOES) + "%")



print ("\n\nMELHOR SOLUÇÃO: \n")

printarTabuleiro(melhor_solucao.tabuleiro)

print ("Custo: %d" %(melhor_solucao.custo))






