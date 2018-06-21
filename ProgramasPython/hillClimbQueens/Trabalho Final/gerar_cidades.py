from random import randint

posicoes = {}

def gerar_posicoes(n_cidades):
	global posicoes
	for x in range(n_cidades):
		posicoes[str(x)] = (randint(10, 200), randint(10, 200))


gerar_posicoes(30)

arq = open("posicoes.txt", "w")

colocar = "{"

for x in posicoes.keys():
	colocar += "'" + x + "'" + ":" + str(posicoes[x]) +","

colocar += "}"


arq.write(colocar)
arq.close()