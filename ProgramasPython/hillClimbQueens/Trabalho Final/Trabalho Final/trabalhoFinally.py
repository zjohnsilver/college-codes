from random import randint, uniform, random
import math
from copy import deepcopy
from viagens import Viagem



n_cidades = 20

""" Vetor para testes com n_cidades = 10"""
posicoes = {'0':(29, 137),'1':(146, 59),'2':(55, 69),'3':(100, 78),'4':(45, 105),'5':(102, 174),
			'6':(191, 71),'7':(17, 21),'8':(34, 158),'9':(132, 36),'10':(188, 100),'11':(124, 13),
			'12':(12, 134),'13':(103, 95),'14':(127, 192),'15':(128, 137),'16':(13, 190),'17':(78, 52),
			'18':(147, 13),'19':(26, 175),'20':(20, 42),'21':(60, 191),'22':(115, 161),'23':(55, 68),'24':(19, 58),
			'25':(86, 197),'26':(198, 19),'27':(51, 112),'28':(154, 113),'29':(44, 200)}



def gerar_posicoes(n_cidades):
	global posicoes
	for x in range(n_cidades):
		posicoes[str(x)] = (randint(10, 200), randint(10, 200))


### Se deseja usar o vetor de testes, comente esta linha
#gerar_posicoes(n_cidades)

def gerarInicio():
	cidades_visitadas = []

	while (1 not in cidades_visitadas) or (2 not in cidades_visitadas) or (3 not in cidades_visitadas):
		cidades_visitadas = []
		for x in range(n_cidades):
			cidades_visitadas.append(randint(1,3))


	caminho = caminho_viajantes(cidades_visitadas, [n_cidades, n_cidades])



	###  Posição no vetor base que se encontra a primeira ocorrência do viajante 1
	posicao_fixa = caminho[0]

	cidade_proxima = menor_distancia(posicao_fixa)


	## Viajante que se encontra na posição da cidade mais próxima
	aux = cidades_visitadas[cidade_proxima]

	## Posição do primeiro viajante 3, para que possa receber o viajante auxiliar
	substituir = cidades_visitadas.index(3)


	## Realizando uma troca justa.

	cidades_visitadas[cidade_proxima] = 3

	cidades_visitadas[substituir] = aux
	

	info = (posicao_fixa, cidade_proxima)

	caminho = caminho_viajantes(cidades_visitadas, info)


	return Viagem(cidades_visitadas, caminho, custo_caminho(caminho)), info




def menor_distancia(cidade):
	custo_menor = 3000000
	for x in range(0, n_cidades):
		if x != cidade:
			## modulo(cidade1[x] - cidade2[x])
			xDistance = math.fabs(posicoes[str(cidade)][0] - posicoes[str(x)][0])

			## modulo(cidade1[y] - cidade2[y])
			yDistance = math.fabs(posicoes[str(cidade)][1] - posicoes[str(x)][1])

			custo = math.sqrt((xDistance**2) + (yDistance**2))

			if custo < custo_menor:
				cidade_proxima = x
				custo_menor = custo

	return cidade_proxima



def caminho_viajantes(cidades_visitadas, info):
	visitas = []

	primeira_cidade = info[0]
	cidade_proxima = info[1]

	if primeira_cidade < n_cidades:
		visitas.append(primeira_cidade)

	for x in range(1, 4):
		for y, c in enumerate(cidades_visitadas):
			if c==(x) and y!=cidade_proxima and y!=primeira_cidade:
				visitas.append(y)

	if cidade_proxima < n_cidades:
		visitas.append(cidade_proxima)

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


def novaRota(vetor_base, info):

	viagens = Viagem(vetor_base)


	mudar_posicao = randint(0, n_cidades-1)

	while (mudar_posicao == info[0] or mudar_posicao == info[1]):
		mudar_posicao = randint(0, n_cidades-1)

	viagens.base[mudar_posicao] = randint(1,3)

	viagens.caminho = caminho_viajantes(viagens.base, info)
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
	taxa = 0.9

	#S0, info = gerarInicio() #Solução Inicial

	S0 = Viagem([3, 2, 3, 2, 3, 1, 2, 2, 3, 1, 3, 2, 3, 3, 1, 1, 2, 2, 2, 2, 3,1, 3, 1, 3, 3, 1, 3, 3, 2], 
				[5, 9, 14, 15, 21, 23, 26, 1, 3, 6, 7, 11, 16, 17, 18, 19, 29, 0, 2, 4, 8, 10, 12, 13, 20, 24, 25, 27, 28, 22],
				3079)
	info = []
	info.append(S0.caminho[0])
	info.append(S0.caminho[-1])

	S = Viagem(deepcopy(S0.base), deepcopy(S0.caminho), S0.custo)

	melhor_solucao = Viagem(deepcopy(S.base), deepcopy(S.caminho), S.custo)

	T = Ti
	while (T > Tf):
		i = 1
		while i <= 100:
			vizinho = novaRota(deepcopy(S.base), info)

			deltaCusto = vizinho.custo - S.custo

			if probabilidade_aceitar(deltaCusto, T) > random():
				S = Viagem(deepcopy(vizinho.base), deepcopy(vizinho.caminho), vizinho.custo)

			if (S.custo < melhor_solucao.custo):
				melhor_solucao = Viagem(deepcopy(S.base), deepcopy(S.caminho), S.custo)

			i+=1

		T *= taxa

	return melhor_solucao


solucao = simulatedAnnealing()

print (solucao.base)
print (solucao.caminho)
print (solucao.custo)
