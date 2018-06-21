from no import No

## Retorna uma string entre dois caracteres dados
def intoCaracters(string, char_a, char_b):
	new_string = ""
	for x in range(len(string)):
		if string[x] == char_a:
			inicio = x+1
			continue
		if string[x] == char_b:
			fim = x
	return string[inicio:fim]


## Le o arquivo mapa.txt
## Salva o arquivo em uma lista com o seguinte formato:
## [nome_no, [lista_de_nos_que_ele_alcanca_em_um_passo]]
def obterMapa(arquivo):
	arq = open(arquivo, "r")

	mapa = arq.read().split("\n")

	dic = {}
	for x in range(len(mapa)):
		mapa[x] = mapa[x].split(":")

		mapa[x][1] = intoCaracters(mapa[x][1], '[', ']')
		mapa[x][1] = mapa[x][1].split(",")

		dic[mapa[x][0]] = mapa[x][1]
	return mapa


## Retorna uma lista com os Nos
def fazerNos(estrutura):
	nos = {}

	for key, valor in estrutura:
		valor = [No(x, key, []) for x in valor]
		nos[key] = valor
	
	return nos