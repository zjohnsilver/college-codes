from estados import estados

objetivo = input("Palavra: ").upper()
dica = input("Dica: ").upper()

print ("\n" * 300)

tamanho_objetivo = len(objetivo)


tracos = ['_'] * len(objetivo)


print (" ----------------------- ")
print ("|                       |")
print ("|     JOGO DA FORCA     |")
print ("|                       |")
print (" ----------------------- ")


LIMITE_JOGADAS = len(objetivo) -1
tentativas = []

### Posicao dos estados
pos = 0

while True:
	# Imprimir jogo
	print('Dica: ' + dica)
	print (estados[pos])

	for y in tracos:
		print (y, end = "   ")

	print("\n\n" + "Tentativas: " + str(tentativas) + "\n")

	#### Verificacoes de vitoria
	if "_" not in tracos:
		print("PARABÉNS, VOCÊ GANHOU")
		break
	#### Se o limite de jogadas for alcançado => FIM
	elif (pos == LIMITE_JOGADAS):
		print ("VOCÊ PERDEU, MAS NÃO DESISTA, TENTE NOVAMENTE")
		break

	#### Recebendo palpite do jogador
	palpite = input("--> ").upper()

	#### Verificando se o palpite esta na palavra
	#### E substituir os tracos correspondentes pelo palpite
	if palpite in objetivo:
		for y in range(len(objetivo)):
			if palpite == objetivo[y]:
				tracos[y] = palpite
	
	#### Se não tiver o palpite, adicioná-lo as tentativas
	else:
		tentativas.append(palpite)
		pos+=1
