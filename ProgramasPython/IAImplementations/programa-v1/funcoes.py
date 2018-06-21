from no import No

## Le o arquivo mapa.txt
## Salva o arquivo em uma lista com o seguinte formato:
## [nome_no, [lista_de_nos_que_ele_alcanca_em_um_passo]]

## Retorna uma lista com os Nos
def fazerNos(arquivo):
	arq = open(arquivo, "r")

	mapa = {}
	for line in arq.readlines():
		linha = line.split()
		
		filhos = []
		for i in range(1, len(linha)):
			filhos.append(linha[i])
		
		mapa[linha[0]] = filhos

	arq.close()

	for key, valor in mapa.items():
		valor = [No(x,key) for x in valor]
		mapa[key] = valor
	
	return mapa

## Busca Custo Uniforme
## Ela assume que alem dos filhos vc tbm escreveu no arquivo
## os custos de ir até esses filhos
def obterMapa(arquivo):
	arquivo = open(arquivo, "r")

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
		
		
	return mapa

## Obter Mapa Bidirecional
def obterMapaBi(arquivo):
	arq = open(arquivo, "r")

	mapa = {}
	for line in arq.readlines():
		linha = line.split()
		
		filhos = []
		for i in range(1, len(linha)):
			filhos.append(linha[i])
		
		mapa[linha[0]] = filhos

	arq.close()

	for key, valor in mapa.items():
		valor = [No(x,key) for x in valor]
		mapa[key] = valor
		
		
	return mapa
		
