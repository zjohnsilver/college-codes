from no import No

objetivo = "Bucharest"

arq = open("HeuristicaBucharest.txt", "r")

## Tabela com as Heuristicas até bucharest
tabela = {}
for line in arq.readlines():
	linha = line.split()
	
	tabela[linha[0]] = int(linha[1])

arq.close()

### Cria um dicionario com todas as cidades e seus custos
arquivo = open("mapaCustos.txt", "r")

############ Criar uma função que leia do arquivo mapa ou do arquivo aspirador
############ Chamar essa função dentro da função Custo Uniforme antes do while
############ Passando como parâmetro dessa função o tipo de pesquisa: romenia ou aspirador

mapa = {}
for line in arquivo.readlines():
	linha = line.split()
	
	mapa[linha[0]] = {}
	
	for i in range(1, len(linha), 2):
		mapa[linha[0]][linha[i]] = int(linha[i+1])

arquivo.close()
		
### Transforma os valores do dicionario em Nos
for key, valor in mapa.items():
	valor = [No(x,key,y) for x,y in valor.items()]
	mapa[key] = valor


def expansao(No):
	expand = []
	## Antes de retornar, setta o pai dos nos expandidos como o no que chegou
	for x in mapa[No.estado]:
		x.pai = No
		x.caminho = No.caminho + x.custo + tabela[No.estado]
		expand.append(x)
		
	return expand
	
def solucao(No, noInicio):
	caminho = []
	while No.estado != noInicio:
		caminho.append(No.estado)
		No = No.pai
	caminho.append(No.estado)
	return caminho[::-1]
	
def buscaA(estadoInicial):
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
	solucao = buscaA('Arad')

	print (solucao)

