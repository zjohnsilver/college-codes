from random import randint, uniform
import math

from copy import deepcopy

from viagens import Viagens


n_cidades = 20



def gerar_distancias(n_cidades):
	distancia_cidades = [[0 for y in range(n_cidades)] for x in range(n_cidades)]

	for x in range(n_cidades):
		for y in range(n_cidades):
			if not distancia_cidades[x][y]: 
				distancia_cidades[x][y] = distancia_cidades[y][x] = randint(20,100)

	return distancia_cidades


distancias = gerar_distancias(n_cidades)


#print (distancias)

"""
distancias = [[41, 81, 86, 45, 21],
			  [81, 90, 96, 97, 76],
			  [86, 96, 43, 24, 49],
			  [45, 97, 24, 82, 33],
			  [21, 76, 49, 33, 54]]


"""
def gerarInicio():
	cidades_visitadas = []

	while (1 not in cidades_visitadas) or (2 not in cidades_visitadas) or (3 not in cidades_visitadas):
		cidades_visitadas = []
		for x in range(n_cidades):
			cidades_visitadas.append(randint(1,3))



	caminho = caminho_viajantes(cidades_visitadas)

	"""
	### Obter a cidade mais próxima da cidade inicial
	menor = max(distancias[caminho[0]])
	cidade = distancias[caminho[0]].index(menor)
	for coluna in range(1, n_cidades):
		if (distancias[caminho[0]][coluna] < menor) and (coluna != caminho[0]):
			menor = distancias[caminho[0]][coluna]
			cidade = coluna

	index_ultima_cidade_visitada = 0
	for i, v in enumerate(cidades_visitadas[::-1]):
		if v==3:
			index_ultima_cidade_visitada = i
			break

	cidades_visitadas[n_cidades-1 -index_ultima_cidade_visitada] = cidades_visitadas[cidade]

	cidades_visitadas[cidade] = 3
	"""

	#caminho = caminho_viajantes(cidades_visitadas)

	return Viagens(cidades_visitadas, caminho, calcula_custo_caminho(caminho, distancias))





def caminho_viajantes(cidades_visitadas):
	visitas = []

	for x in range(1, 4):
		for y, c in enumerate(cidades_visitadas):
			if c==(x):
				visitas.append(y)

	return visitas



def calcula_custo_caminho (caminho, distancia_cidades):
	par = [0, 0]
	custo = 0

	par[0] = caminho[0]

	for x in range(1, len(caminho)):

		par[1] = caminho[x]

		custo += distancia_cidades[par[0]][par[1]]

		par[0] = par[1]

	custo += distancia_cidades[par[1]][caminho[0]]

	return custo


def printar_matriz(matriz):
	for x in matriz:
		for y in x:
			print ("%d"%(y), end = " ")
		print ("")

	return ""


"""
def novaRota(viagens):
	primeiro_um = 0
	ultimo_tres = 0

	um = True
	for x in range(len(viagens.base)):
		if viagens.base == 1 and um:
			primeiro_um = x
			um = False

		if viagens.base == 3:
			ultimo_tres = x


	alterar = randint(0, n_cidades-1)

	while (alterar == primeiro_um) or (alterar == ultimo_tres):
		alterar = randint(0, n_cidades-1)

	base = viagens.base

	base[alterar] = randint(1,3)

	while (1 not in base) or (2 not in base) or (3 not in base):
		base[alterar] = randint(1,3)


	viagens.base = base
	viagens.caminho = caminho_viajantes(viagens.base)
	viagens.custo = calcula_custo_caminho(viagens.caminho, distancias)

	return viagens

 0 1 2 3 4
[2 3 3 1 1]

[2 1 3 3 1]


[3 4 0 1 2]

[1 4 0 2 3]


"""

def novaRota(viagens):
	pos1 = randint(0, n_cidades-1)
	pos2 = randint(0, n_cidades-1)

	cidade1 = viagens.base[pos1]
	cidade2 = viagens.base[pos2]

	viagens.base[pos2] = cidade1
	viagens.base[pos1] = cidade2


	viagens.caminho = caminho_viajantes(viagens.base)
	viagens.custo = calcula_custo_caminho(viagens.caminho, distancias)

	return viagens

def simulatedAnnealing():
	Ti = 10000
	#Ti += Ti * (n_cidades/100.0)
	Tf = 1
	taxa = 0.997


	S0 = gerarInicio() #Solução Inicial
	S = S0 #(Solucao Atual)

	n_iteracoes = 5

	melhor_solucao = S0

	T = Ti
	while (T > Tf):
		for x in range(n_iteracoes):
			vizinho = Viagens()
			vizinho.base = deepcopy(S.base)
			vizinho.caminho = deepcopy(S.caminho)
			vizinho = novaRota(vizinho)

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

			
			print (melhor_solucao.custo)

		T = taxa*T

	return melhor_solucao

#solucao = simulatedAnnealing()


print (printar_matriz(distancias))

for x in range(10):
	solucao = simulatedAnnealing()

	print (solucao.custo)
	print (solucao.caminho)
