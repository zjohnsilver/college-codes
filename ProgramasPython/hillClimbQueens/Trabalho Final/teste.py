from random import randint
from itertools import permutations
import math


posicoes = {'0':(28, 124),'1':(69, 92),'2':(76, 176),'3':(94, 134),
			'4':(158, 147),'5':(37, 193),'6':(39, 42),'7':(134, 180),
			'8':(171, 79),'9':(19, 29)}



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

custo = 2000000
for x in list(permutations(range(10))):
	if custo_caminho(x) < custo:
		melhor_combinacao = x
		custo = custo_caminho(x)

print (melhor_combinacao, custo)