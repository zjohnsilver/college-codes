from funcoes import obterMapa, fazerNos
from no import No
import random

mapa = fazerNos(obterMapa("mapa.txt"))

def busca_largura(estado_inicial, objetivo):
    no = No(estado_inicial)

    if estado_inicial == objetivo:
	    return solucao(no, estado_inicial)

    borda = [no]
    explorados = []

    while True:
    	no = borda.pop(0)
    	explorados.append(no.estado)

    	if no.estado == objetivo:
    		return solucao(no, estado_inicial)[::-1]

    	for filho in expansao(no):
    		if (filho.estado not in explorados) and not inLista(filho, borda): 
    			borda.append(filho)

    	print (borda[0].estado)
	
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
    
    random.shuffle(expand)
    return expand
    

def inLista(elemento, lista):
    for y in lista:
    	if y.estado == elemento.estado:
    		return True

    return False


if __name__ == '__main__':
	
    print (busca_largura('Arad', 'Bucharest'))
