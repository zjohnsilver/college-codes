from random import randint, uniform, random
import math
from copy import deepcopy
from viagens import Viagem



n_cidades = 10

posicoes = {'0':(28, 124),'1':(69, 92),'2':(76, 176),'3':(94, 134),
			'4':(158, 147),'5':(37, 193),'6':(39, 42),'7':(134, 180),
			'8':(171, 79),'9':(19, 29)}



def gerar_posicoes(n_cidades):
	global posicoes
	for x in range(n_cidades):
		posicoes[str(x)] = (randint(10, 200), randint(10, 200))


#gerar_posicoes(n_cidades)

def gerarInicio():
	cidades_visitadas = []

	while (1 not in cidades_visitadas) or (2 not in cidades_visitadas) or (3 not in cidades_visitadas):
		cidades_visitadas = []
		for x in range(n_cidades):
			cidades_visitadas.append(randint(1,3))


	caminho = caminho_viajantes(cidades_visitadas)

	#posicao_fixa = caminho[0]

	#cidade_proxima = menor_distancia(posicao_fixa)


	### Agora, já sabendo qual a cidade mais próxima, basta fixá-la na última posição ###
	### Para fazer isso, não faço ideia
	

	return Viagem(cidades_visitadas, caminho, custo_caminho(caminho))

"""
def menor_distancia(cidade):
	cidade_proxima = 0
	custo_menor = 3000000
	for x in range(1, n_cidades):
		if x != cidade:
			## modulo(cidade1[x] - cidade2[x])
			xDistance = math.fabs(posicoes[str(cidade)][0] - posicoes[str(x)][0])

			## modulo(cidade1[y] - cidade2[y])
			yDistance = math.fabs(posicoes[str(cidade)][1] - posicoes[str(x)][1])

			custo += math.sqrt((xDistance**2) + (yDistance**2))

			if custo < custo_menor:
				cidade_proxima = x
				custo_menor = custo

	return cidade_proxima
"""

def caminho_viajantes(cidades_visitadas):
	visitas = []

	for x in range(1, 4):
		for y, c in enumerate(cidades_visitadas):
			if c==(x):
				visitas.append(y)

	return visitas


def custo_caminho(caminho):
	custo = 0

	cidades = [0, 0]

	cidades[0] = caminho[0]

	for x in range(1, len(caminho)):

		cidades[1] = caminho[x]

		## modulo(cidade1[x] - cidade2[x])
		xDistance = math.fabs(posicoes[str(cidades[0])][0] - posicoes[str(cidades[1])][0])

		## modulo(cidade1[y] - cidade2[y])
		yDistance = math.fabs(posicoes[str(cidades[0])][1] - posicoes[str(cidades[1])][1])

		custo += math.sqrt((xDistance**2) + (yDistance**2))

		cidades[0] = cidades[1]

	return int(custo)



def printar_matriz(matriz):
	for x in matriz:
		for y in x:
			print ("%d"%(y), end = " ")
		print ("")

	return ""


def novaRota(vetor_base):

	viagens = Viagem(vetor_base)

	viagens.base[randint(0, n_cidades-1)] = randint(1,3)

	viagens.caminho = caminho_viajantes(viagens.base)
	viagens.custo = custo_caminho(viagens.caminho)

	return viagens


def probabilidade_aceitar(deltaCusto, temperatura):
	if deltaCusto < 0:
		return 1.0

	else:
		return math.exp(-deltaCusto/temperatura)


def simulatedAnnealing():
	Ti = 1000
	Tf = 1
	taxa = 0.99

	S0 = gerarInicio() #Solução Inicial

	S = Viagem(deepcopy(S0.base), deepcopy(S0.caminho), S0.custo)

	melhor_solucao = Viagem(deepcopy(S.base), deepcopy(S.caminho), S.custo)

	T = Ti
	while (T > Tf):

		i = 1
		while i <= 100:
			nova_solucao = novaRota(deepcopy(S.base))

			deltaCusto = nova_solucao.custo - S.custo

			if probabilidade_aceitar(deltaCusto, T) > random():
				S = Viagem(deepcopy(nova_solucao.base), deepcopy(nova_solucao.caminho), nova_solucao.custo)

			if (S.custo < melhor_solucao.custo):
				melhor_solucao = Viagem(deepcopy(S.base), deepcopy(S.caminho), S.custo)
				print(melhor_solucao.custo)
				print (melhor_solucao.caminho)

			i+=1

		T *= taxa

	return melhor_solucao


for x in range(1):
	solucao = simulatedAnnealing()

	print (solucao.caminho)
	print (solucao.custo)
