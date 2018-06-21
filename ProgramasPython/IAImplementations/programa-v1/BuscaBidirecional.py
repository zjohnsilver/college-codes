from funcoes import obterMapaBi
from no import No
import random

tuplaPosicoes = ()

mapa = {}

def busca_bidirecional(aspirador, estado_inicial, dfs, dfs2, objetivo = None):
	global mapa
	if (aspirador):
		print ("Entrei")
		mapa = obterMapaBi("mapaAspirador.txt")
		objetivo = "ELL"
	else:
		mapa = obterMapaBi("mapa.txt")
	
	
	estado_inicial1 = No(estado_inicial)
	estado_inicial2 = No(objetivo)

	borda = [estado_inicial1]
	borda2 = [estado_inicial2] 
	explorados1 = []
	explorados2 = []


	while True:
		if not borda or not borda2:
			return "Falha"
		if dfs:
			no = borda.pop() ## DFS
		else:
			no = borda.pop(0) ## Largura
		
		if dfs2:
			no2 = borda2.pop() ## DFS
		else:
			no2 = borda2.pop(0) ## Largura
			
		explorados1.append(no.estado)
		explorados2.append(no2.estado)
		
		if comparaBordas(borda, borda2):
			return solucao(borda[tuplaPosicoes[0]], estado_inicial)[::-1] +  solucao(borda2[tuplaPosicoes[1]].pai, objetivo)

		for filho in expansao(no):
			if (filho.estado not in explorados1) and not inLista(filho, borda): 
				borda.append(filho)
				
		for filho in expansao(no2):
			if (filho.estado not in explorados2) and not inLista(filho, borda2): 
				borda2.append(filho)			
	
def solucao(No, noInicio):
	caminho = []
	while No.estado != noInicio:
		caminho.append(No.estado)
		No = No.pai
	caminho.append(No.estado)

	return caminho

    
def expansao(No):
	expand = []
	for x in mapa.get(No.estado):
		x.pai = No
		expand.append(x)
	random.shuffle(expand)
	return expand
    
def comparaBordas(borda1, borda2):
	global tuplaPosicoes
	for x in range(len(borda1)):
		for y in range(len(borda2)):
			if borda1[x].estado == borda2[y].estado:
				tuplaPosicoes = (x, y)
				return True
	return False

def inLista(elemento, lista):
	for y in lista:
		if y.estado == elemento.estado:
			return True
		return False

def main():
	## True True = 2 DFS
	## True False = 1 DFS e 1 BFS
	## False True = 1 BFS e 1 DFS
	## False False = 2 BFS
    print (busca_bidirecional(True, 'ESS', False, True))

