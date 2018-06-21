from itertools import permutations
import math

n_cidades = 10

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

"""
custo = 30000
caminho = []
for x in list(permutations(range(10))):
	custo2 = custo_caminho(x)

	if custo2 < custo:
		caminho = x
		custo = custo2
		print (custo)

"""

caminho = custo_caminho([2, 0, 1, 4, 5, 6, 8, 9, 3, 7])

caminho2 = custo_caminho([2, 0, 1, 4, 8, 9, 3, 5, 6, 7])

print (caminho)

print (caminho2)



