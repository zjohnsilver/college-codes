from no import No
from funcoes import obterMapa

mapa = {}


### Descobre objetivo
def descobre_menor_custo(mapa, cidade):
	menor = mapa[cidade][0].custo
	cidade_objetivo = mapa[cidade][0].estado
	for cidade in mapa[cidade]:
		if cidade.custo < menor:
			menor = cidade.custo
			cidade_objetivo = cidade.estado


	return cidade_objetivo

def expansao(No):
	expand = []
	## Antes de retornar, setta o pai dos nos expandidos como o no que chegou
	for x in mapa[No.estado]:
		x.pai = No
		x.caminho = No.caminho + x.custo
		x.caminho2 = No.caminho2 + [No.estado]
		expand.append(x)
		
	return expand
	
def solucao(No, noInicio):
	caminho = []
	while No.estado != noInicio:
		caminho.append(No.estado)
		No = No.pai
	caminho.append(No.estado)
	return caminho[::-1]
	
def buscaUniforme(estadoInicial):
	global mapa

	mapa = obterMapa("cidades.txt")

	objetivo = descobre_menor_custo(mapa, estadoInicial)
	
	global passo_a_passo
	passo_a_passo = ""
	
	borda = [No(estadoInicial, No(), 0)]
	explorados = []

	i = 0

	while True:
		if not borda:
			return 'Falha', 0, []
		borda.sort(key= lambda No: No.caminho)


		print ('[', end= " ")
		for x in borda:
			print (x.estado, end = " ")
		print (']')

		if (borda[0].estado == objetivo and len(no.caminho2) <9):
			borda[0].caminho += 1000
			continue

		no = borda.pop(0)

		explorados.append(no)
		
		if (no.estado == objetivo and len(no.caminho2) == 9):
			print (no.caminho)
			return solucao(no, estadoInicial), no.caminho, no.caminho2
				
		filhos = expansao(no)


		for filho in filhos:
			## Se filho esta na borda e seu caminho e maior do que o que queremos inserir, substitua ele
			if inLista(filho, borda):
				for x in range(len(borda)):
					if borda[x].estado == filho.estado:
						if borda[x].custo > filho.custo:
							borda[x].pai = filho.pai
							borda[x].caminho = filho.caminho
			if (filho.estado not in no.caminho2):
				borda.append(filho)
		i+=1

def inLista(elemento, lista):
	for y in lista:
		if y.estado == elemento.estado:
			return True
	return False


if __name__ == '__main__':
	solucao = buscaUniforme('AAA')

	print ("Caminho:\n%s\nCusto do Caminho: %d" 
							%(solucao[0], solucao[1] ) ) 


	print (solucao[2])