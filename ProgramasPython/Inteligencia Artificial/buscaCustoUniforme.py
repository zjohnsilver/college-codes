from no import No

mapa_da_romenia = {	'Arad'		: {'Zerind':75, 'Sibiu':140, 'Timisoara':118},
					'Oradea'	: {'Sibiu':151},
					'Zerind'	: {'Oradea':71},
					'Timisoara'	: {'Lugoj':111},
					'Lugoj'		: {'Mehadia':70},
					'Sibiu'		: {'Rimnicu':80, 'Fagaras':99},
					'Fagaras'	: {'Bucharest':211},
					'Mehadia'	: {'Dobreta':75},
					'Dobreta'	: {'Craivoa':120},
					'Craivoa'	: {'Rimnicu':146, 'Pitesti':138},
					'Pitesti'	: {'Bucharest':101},
					'Rimnicu'	: {'Pitesti':97, 'Craivoa':146},
					'Bucharest'	: {'Urziceni':85, 'Giurgiu':90},
					'Urziceni'	: {'Hirsova':98, 'Vaslui':142},
					'Hirsova'	: {'Eforie':86},
					'Vaslui'	: {'Iasi':92},
					'Iasi'		: {'Neamt':87}}
		
### Transforma os valores do dicionario em Nos
for key, valor in mapa_da_romenia.items():
	valor = [No(x,key,y) for x,y in valor.items()]
	mapa_da_romenia[key] = valor
		
objetivo = 'Bucharest'

def expansao(No):
	expand = []
	## Antes de retornar, setta o pai dos nos expandidos como o no que chegou
	for x in mapa_da_romenia[No.estado]:
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
	return caminho
	
def buscaProfundidade(estadoInicial):
	global passo_a_passo
	passo_a_passo = ""
	
	borda = [No(estadoInicial, None, 0)]
	explorados = []

	i = 0

	while True:
		if not borda:
			return 'Falha'
		borda.sort(key= lambda No: No.caminho)
		
		passo_a_passo += "Passo %i"%(i) + "\n"
		for x in borda:
			passo_a_passo += "\t" + str(x.estado) + ": " + str(x.caminho) + "\n"
		passo_a_passo +="\n"
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


def main():
	solucao = buscaProfundidade('Arad')

	solucao = solucao[::-1]

	for e in range(len(solucao)-1):
		print solucao[e]," -> ",
		
	print solucao[e+1]
	
	print "\n"+passo_a_passo
	
main()





