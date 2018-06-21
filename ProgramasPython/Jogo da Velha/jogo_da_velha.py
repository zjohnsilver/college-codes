"""
Programa Super Jogo da Velha: JOGO DA VELHA DE QUALQUER TAMANHO.

Criado no dia 11/05/2016 por Joao Carlos
"""

import sys

def main():
	tabuleiro = []
	tamanho = input("Tamanho: ")  #TAMANHO DO TABULEIRO FORNECIDO PELO TERMINAL
	jogadas = 0 #Contador do jogador >> PAR: Jogador 1 (X) / IMPAR: Jogador 2 (O)
	vitoria = ' '
	
	print ("\n"+"\t"*(tamanho/3) + "********** SUPER JOGO DA VELHA**********\n\n\n")

	gerar_tabuleiro(tabuleiro, tamanho) #Gerando tabuleiro
	menu() #Imprimindo o menu
	mostrar_tabuleiro(tabuleiro, tamanho)  #Mostrando tabuleiro

	while vitoria == ' ': # Laco do jogo
		retorno_pegar_jogada = pegar_jogada(tabuleiro, tamanho, jogadas)
		if (retorno_pegar_jogada == 'C'): #Carregando Jogo
			print ("\n\nJOGO CARREGADO: ")
			try: 
				game = carregar_jogo()
				tabuleiro = game[0]
				tamanho = game[1]
				jogadas = game[2]
			except:  #Caso nao tenha nenhum jogo Salvo...
				print ("Voce nao salvou nenhum jogo\n\n")
				retorno_pegar_jogada = pegar_jogada(tabuleiro, tamanho, jogadas)

		if (retorno_pegar_jogada == 'N'):  #Criando novo Jogo
			print ("\n\nNOVO JOGO: ")
			game = novo_jogo()
			tabuleiro = game[0]
			tamanho = game[1]
			jogadas = game[2]
		print ("\n")
		menu()
		mostrar_tabuleiro(tabuleiro, tamanho)
		vitoria = verifica_vencedor(tabuleiro, tamanho)

		if (retorno_pegar_jogada == 'S'):  #Salvando Jogo
			jogadas-=1

		elif (jogadas == tamanho*tamanho-1 and vitoria == ' '):  #Verificacao de Empate
			print ("Empate !!!")
			ch = raw_input()
			sys.exit()

		jogadas+=1

	if (vitoria == 'X'):
		print ("Jogador 1 Ganhou!!!")
	elif (vitoria == 'O'):
		print ("Jogador 2 Ganhou!!!")

	ch = raw_input()

def gerar_tabuleiro(tabuleiro, tamanho):
	for x in range(tamanho):
		tabuleiro.append([])
		for y in range(tamanho):
			tabuleiro[x].append('%i'%((tamanho*x + y) +1))


def mostrar_tabuleiro(tabuleiro, tamanho):
	for x in range(tamanho):
		print "    "+'\t|   '.join(tabuleiro[x])
		if (not x == tamanho-1):
			print "________" + "|_______"*(tamanho-1)
		else:
			print "\t" + "|\t"*(tamanho-1)

def pegar_jogada(tabuleiro, tamanho, jogador):
	jogada = raw_input("Jogada: ")

	if (jogada == '0'):
		sys.exit("Jogo Encerrado")

	elif (jogada == 'N'): #NOVO JOGO
		return jogada

	elif (jogada == 'S'): #SALVAR JOGO
		salvar_jogo(tabuleiro, tamanho, jogador)
		print ("....JOGO SALVO....")
		return jogada

	elif (jogada == 'C'): #Carregar jogo salvou
		return jogada

	#Verifica se essa jogada ja foi feita
	while (verifica_jogada(tabuleiro, tamanho, jogada) or not(0<int(jogada) <= tamanho*tamanho)):
		print ("Voce nao pode jogar!!!\n\n")
		jogada = raw_input("Jogada: ")

	#Colocar a jogada no local indicado
	for x in range(tamanho):
		for y in range(tamanho):
			if tabuleiro[x][y] == jogada:
				if not (jogador%2):
					tabuleiro[x][y] = 'X'
				else:
					tabuleiro[x][y] = 'O'

def verifica_vencedor(tabuleiro, tamanho):
	#Verificando Linhas
	for x in range(tamanho):
		if (lista_homogenea(tabuleiro[x])):
			return tabuleiro[x][0]

	#Verificando Colunas
	for x in range(tamanho):
		colunas = []
		for y in range(tamanho):
			colunas.append(tabuleiro[y][x])
		if (lista_homogenea(colunas)):
			return colunas[0]

	#Verificando Diagonais
	diagonal = []
	diagonal2 = []
	for x in range(tamanho):
		for y in range(tamanho):
			if (x==y):
				diagonal.append(tabuleiro[x][y])
			if ((x+y) == (tamanho-1)):
				diagonal2.append(tabuleiro[x][y])

	if (lista_homogenea(diagonal)):
		return diagonal[0]
	elif (lista_homogenea(diagonal2)):
		return diagonal2[0]

	return ' '

def lista_homogenea (lista): #Verifica se a lista e homogenea
	for x in lista:
		for y in lista:
			if x==y:
				verifica = 1
			else:
				return 0
	return verifica

def salvar_jogo(matriz, tamanho, jogadas):
	jogo = open('jogo_data.txt', 'w')  #Cria o arquivo

	jogo.write(str(tamanho))
	jogo.write(';' + str(jogadas-1))
	for x in range(tamanho):   		   #Laco para salvar o que ha no tabuleiro
		for y in range(tamanho):
			jogo.write(';' + str(matriz[x][y]))

	jogo.close()  #Fechando documento

def carregar_jogo():
	tabuleiro = []
	
	jogo = open('jogo_data.txt', 'r')  #Lendo arquivo

	game = jogo.readline().split(';')  #Criando uma lista com as jogadas Salvas

	for x in range(int(game[0])):      #Reconstruindo tabuleiro
		tabuleiro.append([])
		for y in range(int(game[0])):
			tabuleiro[x].append(game[(int(game[0])*x+y) +2])

	jogo.close()

	return [tabuleiro, int(game[0]), int(game[1])]  #Returno do tabuleiro, tamanho e qtd_jogadas

def novo_jogo():
	tabuleiro = []
	tamanho = input("Novo Tamanho: ")

	gerar_tabuleiro(tabuleiro, tamanho)  #Gerando tabuleiro Novo

	return [tabuleiro, tamanho, -1]    #Returno do tabuleiro, tamanho e qtd_jogadas

def menu():
	print (" ***** MENU ****** ")
	print ("N - Novo Jogo")
	print ("S - Salvar Jogo")
	print ("C - Carregar Jogo")
	print ("0 - ENCERRAR JOGO\n\n")

def verifica_jogada(matriz, tamanho, jogada):  #Funcao que verifica se a jogada ja foi feita
	for x in range(tamanho):
		for y in range(tamanho):
			if matriz[x][y] == jogada:
				return 0	
	return 1
        
if __name__ == '__main__':
	main()
