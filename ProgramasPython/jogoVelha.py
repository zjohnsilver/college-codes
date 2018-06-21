def menu(menu):
	menutest= True
	while menu == "menu" or menu == "Menu" or menu == "MENU" or menu == "M" or menu == "m" and menutest:
		print ("Menu: ")
		print ("1 - Novo Jogo:")
		print ("2 - Continuar")
		print ("3 - Continuar Jogo Salvo.")
		print ("4 - Salvar")
		print ("5 - Sair do jogo")
		
		opção = int(input("Qual opção deseja: "))	
		print ()
		if opção == 1:
			print ("Novo jogo: \n")
			arquivo = open("gameVelha.txt","w")
			arquivo.close()
			jogadas = [ ["_","_","_"], ["_","_","_"], ["_","_","_"] ] 
			b = [ ["a","b","c"], ["d","e","f"], ["g","h","i"] ]  
			print ("Nome dos jogadores: \n")
			print ()
			player_1 = input("Jogador 1: ")
			player_2 = input("Jogador 2: ")
			print ()
			menutest= False
		if opção == 2:
			menu = ""
		
		if opção ==3:
			jogadas = jogoSalvo()
			player_1, player_2 = jogadores()
		
		if opção == 4:
			print ("Jogo Salvo!")
			menutest= False
		if opção == 5:
			print ("Jogo Encerrado")
			jogando = False
			menutest= False


# Jogo da Velha
print ("          ------------------JOGO DA VELHA------------------")
print ()

#Função da Posição do PONTO E VÍRGULA ( ; )
def pos(z,x): # 1 - Inicio do For, 2 String a ser percorrida
	if z==0:
		for i in range(z,len(x)):
			if x[i] == ";":
				return i
	else:
		for i in range(pos(z-1,x)+1,len(x)):
			if x[i] == ";":
				return i

# Continuar Jogando
jogando = True

def jogoSalvo():  #Recupera as jogadas
	global jogadas
	arquivo = open("gameVelha.txt","r")
	ler = arquivo.readline()
	while ler != "":
		linha = int(ler[0:pos(0,ler)])
		coluna = int(ler[pos(0,ler)+1:pos(1,ler)])
		jogada = ler[pos(1,ler)+1:pos(2,ler)]
		jogadas[linha][coluna] = str(jogada) 
		ler = arquivo.readline()
	arquivo.close()
	return jogadas
	
	
def jogadores():
	arquivo = open("jogadores.txt","r")
	ler = arquivo.readline()
	while ler != "":
		player1 = (ler[0:pos(0,ler)])
		player2 = ler [pos(0,ler)+1: pos(1,ler)]
		ler = arquivo.readline()
	return player1,player2

#Criando arquivo 

#Matriz de Jogadas, Matirz 3 x 3
posições = ["0","1","2"]
jogadas = [ ["_","_","_"], ["_","_","_"], ["_","_","_"] ]   
y=0

print ("Jogador 1: X")
print ("Jogador 2: O\n")

#Pedir aos usuários seus nomes
print ("Nome dos jogadores: \n")
print ()
player_1 = input("Jogador 1: ")
player_2 = input("Jogador 2: ")

arquivo2 = open("jogadores.txt","w")
arquivo2.write(player_1+";"+player_2+";")
arquivo2.close()

print ()
print ("Jogadores, após cada jogada, um espaço vazio será mostrado, Escreva Menu - Para ir ao Menu, ou dê um ENTER para continuar jogando.\n")
#Lista auxiliar, para consertar o problema de comparação da vitória.
b = [ ["a","b","c"], ["d","e","f"], ["g","h","i"] ]  


while jogando:
	arquivo = open("gameVelha.txt","a")
	if y==0:

		print ("   ","  ".join(posições))
		print ()
		for x in range(3):
			print (x," ","  ".join(jogadas[x]))
			print ()
	#Mostrar o jogador da vez
	if y %2 == 0:
		print ("%s é sua vez: "%(player_1))
		print ()
		jogada = "X"
	else:
		print ("%s é sua vez: "%(player_2))
		print ()
		jogada = "O"
	linha = int(input("Linha: "))
	#Caso digite uma linha fora do intervalo permitido 0 a 2
	if linha>2 or linha<0:
		while linha>2 or linha<0:
			print ("Você digitou uma linha fora do intervalo: ")
			linha = int(input("Linha: "))
			print ()
	coluna = int(input("Coluna: "))
	#Caso digite uma coluna fora do intervalo permitido 0 a 2
	if coluna>2 or coluna<0:
		while coluna>2 or coluna<0:
			print ("Você digitou uma coluna fora do intervalo: ")
			coluna = int(input("Coluna: "))
			print ()
	
	
	print ()


	jogadas[linha][coluna] = jogada
	b[linha][coluna] = jogada
	
	arquivo.write(str(linha)+";"+str(coluna)+";"+jogada+";"+"\n")
	
	arquivo.close()
#Imprimindo o jogo da tela	
	print ("   ","  ".join(posições))
	print ()
	for x in range(3):
		print (x," ","  ".join(jogadas[x]))
		print ()

#Condições de vitória
	if y>=4:
		if b[0][0] == b[1][1] == b[2][2] or b[0][0] == b[1][0]== b[2][0] or b[0][0] ==b[0][1]== b[0][2] or b[1][0] == b[1][1]== b[1][2]:
			print ("Jogador %i Venceu."%((y%2)+1))
			jogando = False
		if b[2][0] == b[2][1] == b[2][2] or b[0][1] == b[1][1]== b[2][1] or b[0][2] == b[1][2]== b[2][2] or b[0][2] == b[1][1] == b[2][0]:
			print ("Jogador %i Venceu."%((y%2)+1)) 
			jogando = False
#Empate
	if y ==8:
		print ("DEU VELHA! Ninguém ganhou. ")
		jogando = False
	y+=1
 
	x = input()
	menu(x)




















	
