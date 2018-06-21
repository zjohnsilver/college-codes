from no import No
from funcoes import obterMapa

mapa = {}

def expansao(No):
	expand = []
	## Antes de retornar, setta o pai dos nos expandidos como o no que chegou
	for x in mapa[No.estado]:
		x.pai = No
		x.caminho = No.caminho + x.custo
		expand.append(x)
		
	return expand
	
def solucao(No, noInicio):
	caminho = []
	while No.estado != noInicio:
		caminho.append(No.estado)
		No = No.pai
	caminho.append(No.estado)
	return caminho[::-1]
	
def buscaUniforme(aspirador, estadoInicial, objetivo = None):
	global mapa
	if (aspirador):
		mapa = obterMapa("aspiradorCustos.txt")
	else:
		mapa = obterMapa("mapaCustos.txt")
	
	global passo_a_passo
	passo_a_passo = ""
	
	borda = [No(estadoInicial, None, 0)]
	explorados = []

	i = 0

	while True:
		if not borda:
			return 'Falha'
		borda.sort(key= lambda No: No.caminho)

		no = borda.pop(0)
		explorados.append(no)
		
		if aspirador:
			if no.estado == "DLL" or no.estado == "ELL":
				return solucao(no, estadoInicial)
		else:
			if no.estado == objetivo:
				return solucao(no, estadoInicial)
				
		filhos = expansao(no)
		
		for filho in filhos:
			## Se filho esta na borda e seu caminho e maior do que o que queremos inserir, substitua ele
			if inLista(filho, borda):
				for x in range(len(borda)):
					if borda[x].estado == filho.estado:
						if borda[x].custo > filho.custo:
							borda[x].pai = filho.pai
							borda[x].caminho = filho.caminho
			if not (inLista(filho, borda) or inLista(filho, explorados)):
				borda.append(filho)
		i+=1
		
def inLista(elemento, lista):
	for y in lista:
		if y.estado == elemento.estado:
			return True
	return False


if __name__ == '__main__':
	solucao = buscaUniforme('ESS', 'DLL', True)

	print (solucao)



