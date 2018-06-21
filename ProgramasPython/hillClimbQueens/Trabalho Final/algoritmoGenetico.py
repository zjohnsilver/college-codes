from random import randint, uniform
import math
from copy import deepcopy
from viagens import Viagens
from itertools import permutations


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

	return Viagens(cidades_visitadas, caminho, custo_caminho(caminho))

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





def genetico():
	## Gera população Inicial com caminho e custo
	populacao_inicial = [gerarInicio() for x in range(5)]

	populacao = deepcopy(populacao_inicial)

	contador = 0

	melhor_geral = Viagens(None, None, 3000)

	melhores = {}
	continuar = True
	while (continuar):

		## Organiza a borda pelo fitness
		populacao.sort(key = lambda Viagens: Viagens.custo)

		melhor_anterior = populacao[0]

		if melhor_anterior.custo < melhor_geral.custo:
			melhor_geral = populacao[0]


		"""

			Escolher dois indivíduos da população atual (1 ótimo e 1 ruim)

		"""

		### SELEÇÃO DOS PAIS ###

		pai1 = populacao[0]
		pai2 = populacao[len(populacao)//2]


		### CROSSOVER ###

		# Sortear Posicões dos dois a serem trocadas #
		pos1 = randint(0, n_cidades-1)
		pos2 = randint(0, n_cidades-1)


		### Invertendo bits da posicao 1
		bitEm1 = pai1.base[pos1]
		bitEm2 = pai2.base[pos1]

		filho1 = Viagens(pai1.base)
		filho1.base[pos1] = bitEm2

		filho2 = Viagens(pai2.base)
		filho2.base[pos1] = bitEm1


		### Invertendo bits da posicao 2
		bitEm1 = pai1.base[pos2]
		bitEm2 = pai2.base[pos2]

		filho1 = Viagens(pai1.base)
		filho1.base[pos2] = bitEm2

		filho2 = Viagens(pai2.base)
		filho2.base[pos2] = bitEm1


		### Recalculando atributos dos individuos pais
		filho1.caminho = caminho_viajantes(filho1.base)
		filho1.custo = custo_caminho(filho1.caminho)
		filho2.caminho = caminho_viajantes(filho2.base)
		filho2.custo = custo_caminho(filho2.caminho)

		nova_populacao = [gerarInicio() for x in range(3)]
		nova_populacao.append(filho1)
		nova_populacao.append(filho2)


		nova_populacao.sort(key = lambda Viagens: Viagens.custo)

		melhor_atual = nova_populacao[0]

		if melhor_atual.custo < melhor_geral.custo:
			melhor_geral = Viagens()
			melhor_geral.base = deepcopy(melhor_atual.base)
			melhor_geral.caminho = deepcopy(melhor_atual.caminho)
			melhor_geral.custo = melhor_atual.custo


		populacao = deepcopy(nova_populacao)


		if (str(melhor_geral) in melhores):
			melhores[str(melhor_geral)] +=1
		else:
			melhores[str(melhor_geral)] = 1

		for i in melhores.values():
			if i == 3000:
				continuar = False

	return melhor_geral


for i in range(10):
	solucao = genetico()

	print (solucao.caminho, solucao.custo)