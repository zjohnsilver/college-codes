from no import No

objetivo = 'Bucharest'

arq = open("HeuristicaBucharest.txt", "r")

## Tabela com as Heuristicas até bucharest
tabela = {}
for line in arq.readlines():
	linha = line.split()
	
	tabela[linha[0]] = int(linha[1])

arq.close()

arq = open("mapa.txt", "r")

mapa = {}
for line in arq.readlines():
	linha = line.split()
	
	filhos = []
	for i in range(1, len(linha)):
		filhos.append(linha[i])
	
	mapa[linha[0]] = filhos

arq.close()

for key, valor in mapa.items():
	valor = [No(x,key) for x in valor]
	mapa[key] = valor
	
	
def buscaGulosa(estadoInicial):
	no = No(estadoInicial)

	if estadoInicial == objetivo:
		return solucao(no, estadoInicial)

	borda = [no]

	while True:
		if not borda:
			return 'Falha'
		
		menor = borda[0]
		# Descobrindo quem tem menor heuristica
		for x in range (len(borda)):
			if tabela[borda[x].estado] <= tabela[menor.estado]:
				menor = borda[x]
				indice = x
		aux = borda[indice]
		borda[indice] = borda[0]
		borda[0] = aux
		
		no = borda.pop(0)

		for filho in expansao(no):
			if not inLista(filho, borda):
				if filho.estado == objetivo:
					return solucao(filho, estadoInicial)[::-1]
				borda.append(filho)

def solucao(No, noInicio):
	caminho = []
	while No.estado != noInicio:
		caminho.append(No.estado)
		No = No.pai
	caminho.append(No.estado)
	return caminho

def expansao(No):
	expand = []
	## Antes de retornar, setta o pai dos nos expandidos como o no que chegou
	for x in mapa.get(No.estado):
		x.pai = No
		expand.append(x)
		
	return expand

def inLista(elemento, lista):
	for y in lista:
		if y.estado == elemento.estado:
			return True
	return False

if __name__ == '__main__':
	print (buscaGulosa('Arad'))





