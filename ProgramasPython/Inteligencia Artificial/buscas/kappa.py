from funcoes import obterMapa, fazerNos
from no import No

mapa = fazerNos(obterMapa("mapa.txt"))

def busca_largura(estado_inicial, objetivo):
    no = No(estado_inicial)

    if estado_inicial == objetivo:
	    return solucao(no, estado_inicial)

    borda = [no]
    explorados = []

    while True:
        if not borda:
	    return ('Falha')
	no = borda.pop(0)
	explorados.append(no.estado)

	for filho in expansao(no):
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

def main():	
	
    print (busca_largura('Arad', 'Bucharest'))

main()
