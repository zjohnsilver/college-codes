# Jogo Simples de Ataque e Cura

#importa o modulo random
import random

#armazena a vida do player
player_vida = 500

#armazena o sp do player
player_sp = 100

#vida padrao de um inimigo
inimigo_vida = 50

#determina o numero de inimigos
n = input("Digite o numero de inimigos: ")

#vetor que armazena todos os inimigos

inimigos = []

# adicionamos ao vetor um vetor com 2 componentes: o numero do inimigo e sua vida
for i in range(n):
	inimigos.append([i+1,inimigo_vida])

#Enquanto essa variavel for True estaremos executando o jogo
jogando = True

while jogando: #Nosso loop do jogo 
	#Imprimimos na tela a vida
	print "Vida:",player_vida
	#e o sp do player
	print "SP:",player_sp

	#Pedimos para o player escolher o que fazer
	atk = input("Deseja atacar (1), ou curar (2): ")

	#se ele escolher atacar, devemos:
	if atk == 1:
		#escolher aleatoriamente um inimigo para ser atacado
		selecionado = random.choice(inimigos)
		#determinar o dano causado
		dano = random.randint(10,15)
		#imprimir essas informacoes para o usuario
		print "Causou %i de dano ao inimigo %i!"%(dano,selecionado[0])
		#diminuir da vida do inimigo o dano
		selecionado[1] -= dano
		# se a vida do inimigo for zerada, devemos:
		if selecionado[1] <=0: 
			#dizer que o inimigo morreu
			print "Inimigo %i morreu!"%selecionado[0]
			# e remover esse inimigo da lista de inimigos
			inimigos.remove(selecionado)
	#caso contrario ele escolheu curar
	else: 
		#so podemos curar se o sp do player for maior do que 10
		if player_sp>=10:
			#escolhemos um valor aleatorio para a cura
			cura = random.randint(10,15)
			#imprimimos o quanto o player recebeu de cura
			print "Voce recebeu %i de vida!"%(cura)
			#adicionamos isso a vida do player
			player_vida+=cura
			#e diminuimos em 10 o sp do player
			player_sp-=10
		#se o player tiver menos de 10 de sp
		else:
			#imprimimos que o player nao pode se curar
			print "SP insuficiente."
	#depois disso e a vez dos inimigos atacarem
	for inimigo in inimigos:
		#escolhemos se o inimigo vai acertar ou errar
		#o inimigo tem 75% de chance de acertar
		#bool retorna True, se encontrar o elemento 1, e False se encontrar o elemento 0
		acertou = bool(random.choice([1,1,1,0]))
		#se ele acertar, devemos:
		if acertou:
			#escolher um dano causado ao player
			dano = random.randint(1,3)
			#imprimir a msg de dano
			print "Inimigo %i causou %i de dano!"%(inimigo[0], dano)
			#diminuir a vida do player
			player_vida-=dano
		#caso contrario
		else:
			print "Inimigo %i errou o ataque!"%(inimigo[0])
	#depois devemos aumentar o sp do player
	if player_sp<100:
		#aumentamos em 3 toda rodada
		player_sp+=3
	#sp nao pode ser maior que 100
	if player_sp>100:
		player_sp=100 
	
	#se a vida for menor que 0 ele perdeu
	if player_vida<=0:
		print "Perdeu o jogo!"
		jogando = False
	#se o numero de inimigos for 0 venceu
	if len(inimigos) == 0:
		print "Parabens voce ganhou o jogo!"
		jogando = False 
	
	


































