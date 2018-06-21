from funcoes import obterMapa, fazerNos
from no import No

mapa = fazerNos(obterMapa("mapa.txt"))

def busca_profund_limitada(estado_inicial, objetivo, limite):
	no = No(estado_inicial)

	borda = [no]

	if no.estado == objetivo:
		return solucao(no, estado_inicial)[::-1]		

	while True:
		if not borda:
			return "Falha"

		no = borda.pop()

		for filho in expansao(no):
			if filho.estado == objetivo:
				return solucao(filho, estado_inicial)[::-1]
			borda.append(filho)
		## Testando se a profundidade dos filhos ja e a profundidade limite
		if limite == no.profundidade + 1: 
			return "Limite alcancado, voce nao encontrou a solucao, tente um valor mais alto"

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
		x.profundidade+=1
		x.pai = No
		expand.append(x)
		
	return expand

def main():
	inicio = raw_input("Inicio: ")
	final = raw_input("Final: ")
	limite = input("Limite: ")
	print busca_profund_limitada(inicio, final, limite)

main()
