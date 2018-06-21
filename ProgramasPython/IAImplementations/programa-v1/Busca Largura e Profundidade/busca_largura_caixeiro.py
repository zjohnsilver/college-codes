from funcoes import obterMapa, fazerNos
from no import No
import random

#mapa = fazerNos(obterMapa("cidades.txt"))

mapa = ['AAA', 'AAB', 'AAC', 'AAD', 'AAE', 'AAF', 'AAG', 'AAH', 'AAI', 'AAJ', 'AAK', 'AAL']

def busca_largura(estado_inicial, objetivo):
    no = No(estado_inicial)

    if estado_inicial == objetivo:
	    return solucao(no, estado_inicial)

    borda = [no]

    while True:
    	no = borda.pop(0)

    	if (len(no.caminho2) == 11) and (no.estado == objetivo):
    		return solucao(no, estado_inicial)[::-1]

    	for filho in expansao(no):
    		if (filho.estado not in filho.caminho2): 
    			borda.append(filho)

    	print (no.caminho2)
	
def solucao(No, noInicio):
	caminho = []
	while No.estado != noInicio:
		caminho.append(No.estado)
		No = No.pai
	
	caminho.append(No.estado)
	
	return caminho


def expansao(n):
    expand = []
    ## Antes de retornar, setta o pai dos nos expandidos como o no que chegou
    for x in mapa:
        x = No(x)
        if x != n.estado:
            x.pai = n
            x.caminho2 = n.caminho2 + [n.estado]
            expand.append(x)
    
    random.shuffle(expand)
    return expand
    

def inLista(elemento, lista):
    for y in lista:
    	if y.estado == elemento.estado:
    		return True

    return False


if __name__ == '__main__':
	
    print (busca_largura('AAA', 'AAF'))
