""" JOGO DA VELHA -- LANCELOT

	Criado no dia 7 de Junho de 2016 """


#Importando funcoes

from lancelot_functions import funcoes

import sys

def main():

	print "\n#######  JOGO DA VELHA #######\n"

	jogadas = 1 #Variavel que conta as jogadas
	
	#Tabuleiro do jogo - 1 a 9
	tabuleiro = [str(x) for x in range(1, 10)]

	#comeco = raw_input("Quer comecar? ( S/N ): ")

	print ""
	
	"""simbolo = raw_input("Jogar com (X / O): ")

	if (simbolo == 'X'):
		simbolo2 = 'O'
	else:
		simbolo2 = 'X'
	"""
	#Mostrar tabuleiro
	funcoes.mostrar_tabuleiro(tabuleiro)

	#Tabuleiro do jogo zerado
	tabuleiro = [x for x in "         "]

	#Laco do jogo
	while (jogadas<=5):
		#Pegar jogada
		jogada = funcoes.jogar()

		# Caso voce ja tenha jogado naquele lugar
		while jogada<1 or jogada>9 or tabuleiro[jogada-1] != ' ':
			print ("\nJogada invalida!" )
			jogada = funcoes.jogar()

		tabuleiro[jogada-1] = 'X'
		jogada_lancelot = funcoes.lancelot_jogada(tabuleiro)

		print jogada_lancelot

		#Pondo a jogada no tabuleiro	
		tabuleiro[jogada_lancelot] = 'O'

		# Mostrando tabuleiro
		funcoes.mostrar_tabuleiro(tabuleiro)

		#Vericiando vitoria
		verificar =	funcoes.verificar_vitoria(tabuleiro)

		#Mostrando ganhador
		if (verificar == 'X'):
			print ("Voce ganhou !!")
			break

		elif (verificar == 'O'):
			print ("\nLancelot ganhou !!")
			break

		if jogadas == 5:
			sys.exit("\n\tEMPATE\n");

		jogadas+=1



if __name__ == "__main__":
	main()

