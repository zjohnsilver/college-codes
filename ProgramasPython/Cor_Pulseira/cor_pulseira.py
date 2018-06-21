"""
PROGRAMA PARA SELECIONAR QUAL COR DE PULSEIRA DEVO USAR.

"""

import random, sys

cores = ["preta", "marrom", "azul", "laranja", "lilas", "verde", "vermelha"]

def cor_pulseira(cores):
	cor_escolhida = random.choice(cores)
	cores_new = []

	for cor in cores:
		if cor != cor_escolhida:
			cores_new = cor

	return cor_escolhida


def main():
	cores_arquivo = []
	lista_cores = []

	arquivo = open("cores.txt", "r")

	# Adicionando em uma lista as cores do arquivo
	for cor in arquivo.readlines():
		cores_arquivo.append(cor.split("\n")[0])

	arquivo.close()

	for cor in cores:
		if cor not in cores_arquivo:
			lista_cores.append(cor)

	try:
		cor_escolhida = cor_pulseira(lista_cores)
	except:
		arquivo = open("cores.txt", "w")	
		arquivo.close()
		sys.exit("Execute Novamente o Programa")
	
	arquivo = open("cores.txt", "a")
	arquivo.write(cor_escolhida + "\n")

	print "Cor Escolhida: %s" %(cor_escolhida)

main()