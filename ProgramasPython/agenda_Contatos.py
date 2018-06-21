

### AGENDA DE CONTATOS ###

### JOAO CARLOS DE QUEIROZ PRATA ### 

### DATA: 11 / 06 / 2016 ###

### AINDA FALTA SALVAR A AGENDA EM UM ARQUIVO, E RECUPERÁ-LA ###


def main():
	contatos = []
	while True:
		opcao = menu()

		if opcao == 1:
			contatos.append(adicionar_contato())
			espera = input()

		elif opcao == 2:
			print (remover_contato(contatos))
			espera = input()

		elif opcao == 3:
			print (procurar_contato(contatos))

			espera = input()

		elif opcao == 4:
			print (mostrar_agenda(contatos))
			espera = input()

		elif opcao == 5:
			print ("AGENDA ENCERRADA")
			break


def menu():
	print ("\t\t////////// AGENDA //////////\n")
	print ("1 - Adicionar Contato")
	print ("2 - Remover Contato")
	print ("3 - Procurar Contato")
	print ("4 - Visualizar Agenda")
	print ("5 - Fechar Agenda")

	opcao = int(input("\n>> "))

	return opcao

#Cria um dicionario com as informações dos contatos e o retorna
def adicionar_contato (): 
	dicionario = {}
	print ("Novo Contato: ")
	dicionario["Nome"] = input("Nome: ")
	dicionario["Telefone"] = int(input("Telefone: "))
	dicionario["Endereço"] = input("Endereço: ")
	dicionario["Email"] = input("Email: ")

	print("")

	return dicionario

#Remove contato pelo nome
def remover_contato (contatos):
	contato = input("Remover: ")
	for y in range(len(contatos)):
		if contatos[y]["Nome"].lower() == contato.lower():
			posicao = y
			break

	try:
		del contatos[posicao]
		return ("Contato %s removido.\n" %(contato))

	except:
		return ("\nContato não encontrado.")

#Procura contato pelo nome
def procurar_contato (contatos):
	contato = input("Procurar: ")
	retorno = False
	for contact in contatos:
		if contact["Nome"].lower() == contato.lower():
			print ("Nome:     ", contatos[y]["Nome"])
			print ("Telefone: ",contatos[y]["Telefone"])
			print ("Endereço: ",contatos[y]["Endereço"] )
			print ("Email:    ",contatos[y]["Email"])
			print ("\n")
			retorno = True
			break

	if not retorno:
		return ("\nContato não encontrado.")
	return ("")

#Mostra toda a agenda de contatos
def mostrar_agenda (contatos):
	if contatos != []:
		print ("\t\t////////// CONTATOS //////////\n")
		lista_Nomes = []

		#Adicionando nomes a uma lista para poder ordená-la
		for valor in range(len(contatos)):
			lista_Nomes.append(contatos[valor]["Nome"])

		#Ordenando a lista que contém o nome dos contatos
		lista_Nomes.sort()

		# Percorrendo contatos e imprimindo suas informações
		for nome in lista_Nomes: #lista_Nomes contem os nomes dos contatos
			for y in range(len(lista_Nomes)):
				if contatos[y]["Nome"] == nome: #Quando encontrar o nome correspondente na lista_Nomes, imprima suas informações
					print ("Nome:     ", contatos[y]["Nome"])
					print ("Telefone: ",contatos[y]["Telefone"])
					print ("Endereço: ",contatos[y]["Endereço"] )
					print ("Email:    ",contatos[y]["Email"])
					print ("\n")
					break
		return ("")

	else:
		return ("Você ainda não adicionou nenhum contato.")


main()