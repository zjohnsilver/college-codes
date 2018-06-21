from no import No

mapa_da_romenia = {	'Oradea'	: ['Zerind', 'Sibiu'],
					'Zerind'	: ['Arad', 'Oradea'],
					'Arad'		: ['Zerind', 'Sibiu', 'Timisoara'],
					'Timisoara'	: ['Arad', 'Lugoj'],
					'Lugoj'		: ['Timisoara', 'Mehadia'],
					'Sibiu'		: ['Oradea', 'Arad', 'Rimnicu', 'Fagaras'],
					'Fagaras'	: ['Sibiu', 'Bucharest'],
					'Mehadia'	: ['Lugoj', 'Dobreta'],
					'Dobreta'	: ['Mehadia', 'Craivoa'],
					'Craivoa'	: ['Dobreta', 'Rimnicu', 'Pitesti'],
					'Pitesti'	: ['Craivoa', 'Rimnicu', 'Bucharest'],
					'Rimnicu'	: ['Sibiu', 'Pitesti', 'Craivoa'],
					'Bucharest'	: ['Fagaras', 'Pitesti', 'Urziceni', 'Giurgiu'],
					'Urziceni'	: ['Bucharest', 'Hirsova', 'Vaslui'],
					'Hirsova'	: ['Eforie', 'Urziceni'],
					'Vaslui'	: ['Iasi', 'Urziceni'],
					'Iasi'		: ['Neamt', 'Vaslui']}
		
### Transforma os valores do dicionario em Nos
for key, valor in mapa_da_romenia.items():
	valor = [No(x) for x in valor]
	mapa_da_romenia[key] = valor
		
visitados = [] ## Lista de visitados, para que nao haja repeticoes
objetivo = 'Bucharest'

def expansao(No):
	## Busca a expansao do No no dicionario
	expand = [x for x in mapa_da_romenia[No.estado] if x not in visitados]
	## Antes de retornar, setta o pai dos nos expandidos como o no que chegou
	for x in expand:
		x.pai = No
	return expand
	
def solucao(No, noInicio):
	caminho = []
	while No.estado != noInicio:
		caminho.append(No.estado)
		No = No.pai
	caminho.append(No.estado)
	return caminho
	
def buscaProfundidade(estadoInicial):
	global visitados
	borda = visitados = [No(estadoInicial)]
	
	while True:
		if not borda:
			return 'Falha'
		no = borda.pop()
		if no.estado == objetivo:
			return solucao(no, estadoInicial)
			
		acoes = expansao(no)
		
		borda += acoes
		visitados += acoes
		
			
print buscaProfundidade('Arad')
