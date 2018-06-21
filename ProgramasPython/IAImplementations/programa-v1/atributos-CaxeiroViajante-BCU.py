from random import randint




n_cidades = 10

"""

def soma_vetor(lista):
	soma = 0

	for x in lista:
		soma+=x

	return soma

comerciantes = []

while soma_vetor(comerciantes) < n_cidades and len(comerciantes) < 3:
	comerciantes = []

	quanto_falta = n_cidades

	for x in range(3):

		### Exceção é lançada quando quanto_falta = 0
		### Isso acontece, quando antes de sortear
		### os 3 números, a soma 2 ou menos já for o
		### número de cidades
		try:
			comerciantes.append(randint(5,quanto_falta))
		except ValueError:
			break
		quanto_falta -= comerciantes[x]



print (comerciantes)

"""


########## GERA VETOR COM NOME DE CIDADES ##########

vetor_cidades = []

cidade = "AAA"

for x in range(n_cidades):
	if not (x % 26) and x!=0:
		if not (x % 676):
			cidade = chr(ord(cidade[0]) + 1) + 'A' + 'A'
		else:
			cidade = cidade[:1] + chr(ord(cidade[1]) + 1) + 'A'
	
	vetor_cidades.append(cidade)

	cidade = cidade[:2] + chr(ord(cidade[2]) + 1)

########################



################   GERA ARQUIVO COM CIDADES E SEUS CUSTOS ###############

arquivo = open("cidades.txt", "w")

cidade = "AAA"

cidades = ""

for x in range(n_cidades):
	if not (x % 26) and x!=0:
		if not (x % 676):
			cidade = chr(ord(cidade[0]) + 1) + 'A' + 'A'
		else:
			cidade = cidade[:1] + chr(ord(cidade[1]) + 1) + 'A'
	
	cidades+= cidade + "\t"

	x = 0
	for y in range(n_cidades -1):
		if cidade == vetor_cidades[x]:
			x+=1
			
		cidades += vetor_cidades[x] + " " +str(randint(5,20)) + "\t"

		x+=1
	cidades+="\n"

	cidade = cidade[:2] + chr(ord(cidade[2]) + 1)



arquivo.write(cidades)

arquivo.close()



"""

def descobre_menor_custo(mapa, cidade):
	menor = mapa[cidade][0].custo
	cidade_objetivo = cidade
	for cidade in mapa[cidade]:
		if cidade.custo < menor:
			menor = cidade.custo
			cidade_objetivo = cidade.estado


	return cidade_objetivo


print (descobre_menor_custo())
"""