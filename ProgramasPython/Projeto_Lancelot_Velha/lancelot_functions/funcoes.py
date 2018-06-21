""" Arquivo com as funcoes do programa 
		JOGO DA VELHA LANCELOT 

	Criado no dia 7 de Junho de 2016 """


import random
import sys

def mostrar_tabuleiro (tabuleiro):
	print   " "+" | ".join(tabuleiro[0:3])
	print "___|___|___"
	print   " "+" | ".join(tabuleiro[3:6])
	print "___|___|___"
	print " " + " | ".join(tabuleiro[6:9])
	print "   |   |   "


def verificar_vitoria (tabuleiro):
	if (tabuleiro[0] != ' '):
		if (tabuleiro[0] == tabuleiro[1] == tabuleiro [2]) or (tabuleiro[0] == tabuleiro[3] == tabuleiro [6]) or (tabuleiro[0] == tabuleiro[4] == tabuleiro [8]):
			if (tabuleiro[0] == 'X'):
				return 'X'
			else:
				return 'O' 

	if (tabuleiro[2] != ' '):
		if (tabuleiro[2] == tabuleiro[4] == tabuleiro [6]) or (tabuleiro[2] == tabuleiro[5] == tabuleiro [8]):
			if (tabuleiro[2] == 'X'):
				return 'X'
			else:
				return 'O' 	

	if (tabuleiro[3]!= ' '):
		if (tabuleiro[3] == tabuleiro[4] == tabuleiro [5]):	
			if (tabuleiro[3] == 'X'):
				return 'X'
			else:
				return 'O' 

	if (tabuleiro[6] != ' '):
 		if (tabuleiro[6] == tabuleiro[7] == tabuleiro [8]):	
			if (tabuleiro[6] == 'X'):
				return 'X'
			else:
				return 'O' 
def jogar():
	while True:
		try:
			jogada = int(input("Sua jogada? 1-9: "))
			break
		except:
			print "\nJogada Invalida"

	return jogada

def lancelot_jogada(tabuleiro):
	## Para fazer essa funcao para O e X, eu devo receber na funcao as variaveis simbolo e simbolo2;

	jogadas = []

	if ((tabuleiro[0] == tabuleiro[1] == 'O') and tabuleiro[2] == ' ') or ((tabuleiro[5] == tabuleiro[8] == 'O') and tabuleiro[2] == ' ') or ((tabuleiro[6] == tabuleiro[4] == 'O') and tabuleiro[2] == ' '):
		posicao = 2
		return posicao

	if ((tabuleiro[0] == tabuleiro[2] == 'O') and tabuleiro[1] == ' ') or ((tabuleiro[7] == tabuleiro[4] == 'O') and tabuleiro[1] == ' '):
		posicao = 1
		return posicao

	if ((tabuleiro[2] == tabuleiro[1] == 'O') and tabuleiro[0] == ' ') or ((tabuleiro[3] == tabuleiro[6] == 'O') and tabuleiro[0] == ' ') or ((tabuleiro[8] == tabuleiro[4] == 'O') and tabuleiro[0] == ' '):
		posicao = 0
		return posicao

	if ((tabuleiro[0] == tabuleiro[3] == 'O') and tabuleiro[6] == ' ') or ((tabuleiro[7] == tabuleiro[8] == 'O') and tabuleiro[6] == ' ') or ((tabuleiro[2] == tabuleiro[4] == 'O') and tabuleiro[6] == ' '):
		posicao = 6
		return posicao

	if ((tabuleiro[0] == tabuleiro[6] == 'O') and tabuleiro[3] == ' ') or ((tabuleiro[4] == tabuleiro[5] == 'O') and tabuleiro[3] == ' '):
		posicao = 3
		return posicao

	if ((tabuleiro[1] == tabuleiro[4] == 'O') and tabuleiro[7] == ' ') or ((tabuleiro[6] == tabuleiro[8] == 'O') and tabuleiro[7] == ' '):
		posicao = 7
		return posicao

	if ((tabuleiro[1] == tabuleiro[7] == 'O') and tabuleiro[4] == ' ') or ((tabuleiro[3] == tabuleiro[5] == 'O') and tabuleiro[4] == ' '):
		posicao = 4
		return posicao

	if ((tabuleiro[2] == tabuleiro[5] == 'O') and tabuleiro[8] == ' ') or ((tabuleiro[6] == tabuleiro[7] == 'O') and tabuleiro[8] == ' ') or ((tabuleiro[0] == tabuleiro[4] == 'O') and tabuleiro[8] == ' '):
		posicao = 8
		return posicao

	if ((tabuleiro[2] == tabuleiro[8] == 'O') and tabuleiro[5] == ' ') or ((tabuleiro[3] == tabuleiro[4] == 'O') and tabuleiro[5] == ' '):
		posicao = 5
		return posicao

	if ((tabuleiro[0] == tabuleiro[8] == 'O') and tabuleiro[4] == ' ') or ((tabuleiro[6] == tabuleiro[2] == 'O') and tabuleiro[4] == ' '):
		posicao = 4
		return posicao



	if ((tabuleiro[0] == tabuleiro[1] == 'X') and tabuleiro[2] == ' ') or ((tabuleiro[5] == tabuleiro[8] == 'X') and tabuleiro[2] == ' ') or ((tabuleiro[6] == tabuleiro[4] == 'X') and tabuleiro[2] == ' '):
		posicao = 2
		return posicao

	if ((tabuleiro[0] == tabuleiro[2] == 'X') and tabuleiro[1] == ' ') or ((tabuleiro[7] == tabuleiro[4] == 'X') and tabuleiro[1] == ' '):
		posicao = 1
		return posicao

	if ((tabuleiro[2] == tabuleiro[1] == 'X') and tabuleiro[0] == ' ') or ((tabuleiro[3] == tabuleiro[6] == 'X') and tabuleiro[0] == ' ') or ((tabuleiro[8] == tabuleiro[4] == 'X') and tabuleiro[0] == ' '):
		posicao = 0
		return posicao

	if ((tabuleiro[0] == tabuleiro[3] == 'X') and tabuleiro[6] == ' ') or ((tabuleiro[7] == tabuleiro[8] == 'X') and tabuleiro[6] == ' ') or ((tabuleiro[2] == tabuleiro[4] == 'X') and tabuleiro[6] == ' '):
		posicao = 6
		return posicao

	if ((tabuleiro[0] == tabuleiro[6] == 'X') and tabuleiro[3] == ' ') or ((tabuleiro[4] == tabuleiro[5] == 'X') and tabuleiro[3] == ' '):
		posicao = 3
		return posicao

	if ((tabuleiro[1] == tabuleiro[4] == 'X') and tabuleiro[7] == ' ') or ((tabuleiro[6] == tabuleiro[8] == 'X') and tabuleiro[7] == ' '):
		posicao = 7
		return posicao

	if ((tabuleiro[1] == tabuleiro[7] == 'X') and tabuleiro[4] == ' ') or ((tabuleiro[3] == tabuleiro[5] == 'X') and tabuleiro[4] == ' '):
		posicao = 4
		return posicao

	if ((tabuleiro[2] == tabuleiro[5] == 'X') and tabuleiro[8] == ' ') or ((tabuleiro[6] == tabuleiro[7] == 'X') and tabuleiro[8] == ' ') or ((tabuleiro[0] == tabuleiro[4] == 'X') and tabuleiro[8] == ' '):
		posicao = 8
		return posicao

	if ((tabuleiro[2] == tabuleiro[8] == 'X') and tabuleiro[5] == ' ') or ((tabuleiro[3] == tabuleiro[4] == 'X') and tabuleiro[5] == ' '):
		posicao = 5
		return posicao

	if ((tabuleiro[0] == tabuleiro[8] == 'X') and tabuleiro[4] == ' ') or ((tabuleiro[6] == tabuleiro[2] == 'X') and tabuleiro[4] == ' '):
		posicao = 4
		return posicao


	for x, jogada in enumerate(tabuleiro):
		if jogada == ' ':
			jogadas.append(x)

	if jogadas != []:
		return random.choice (jogadas)
	else:
		mostrar_tabuleiro(tabuleiro)
		sys.exit("\n\tEMPATE\n")

