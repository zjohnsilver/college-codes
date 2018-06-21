from funcoes import obterMapa, fazerNos
from no import No

mapa = fazerNos(obterMapa("mapa.txt"))

def busca_profundidade(estado_inicial, objetivo):

	borda = [No(estado_inicial)]

	while True:
		if not borda:
			return 'Falha'
		no = borda.pop()

		if no.estado == objetivo:
			return solucao(no, estado_inicial)[::-1]
		

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

def main():
	inicio = raw_input("Inicio: ")
	final = raw_input("Final: ")	
	
	print busca_profundidade(inicio, final)

main()
