#from funcoes import *
from copy import deepcopy
from viagens import Viagem
from random import randint
import math


n_cidades = 10

posicoes = {'0':(28, 124),'1':(69, 92),'2':(76, 176),'3':(94, 134),
			'4':(158, 147),'5':(37, 193),'6':(39, 42),'7':(134, 180),
			'8':(171, 79),'9':(19, 29)}

def vizinho(viagem):
	melhor = Viagem(None, None, 10000000)

	for x in range(len(viagem.base)):
		teste = deepcopy(viagem.base)
		for y in range(1,4):
			if y != viagem.base[x]:
				teste[x] = y
				custo = custo_caminho(caminho_viajantes(teste))

				if custo < melhor.custo:
					melhor.base = teste
					melhor.custo = custo
	return melhor


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

	return Viagem(cidades_visitadas, caminho, custo_caminho(caminho))


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


#solucao = vizinho(Viagem([1,3,1,1,2,3]))

#print (solucao.custo)

#solucao2 = vizinho(solucao)

#print (solucao2.custo)



def hillClimb():
	viagem = gerarInicio()

	while (1):

		proximo = vizinho(viagem)

		if (proximo.custo >= viagem.custo):
			return viagem
		viagem = proximo


TOTAL_EXECUCOES = int(input("\nTotal Execuções: "))
custos = {}

i = 0
while (TOTAL_EXECUCOES>i):
	print ("\nExecução: %d" %(i))

	solucao = hillClimb()
	custo = solucao.custo

	print ("\tCusto: %d" %(custo))

	if (i==0):
		melhor_solucao = Viagem()
		melhor_solucao.base = deepcopy(solucao.base)
		melhor_solucao.custo = custo

	elif custo < melhor_solucao.custo:
		melhor_solucao.base = deepcopy(solucao.base)
		melhor_solucao.custo = custo


	if (str(custo) in custos):
		custos[str(custo)] +=1
	else:
		custos[str(custo)] = 1

	i+=1


print ("\n\nTabela de Custos\n")

for i in custos.keys():
	print ("Custos de " + i + ": " + str((custos[i]*100)/TOTAL_EXECUCOES) + "%")


print ("\n\nMELHOR SOLUÇÃO: \n")

print ("Custo: %d" %(melhor_solucao.custo))
