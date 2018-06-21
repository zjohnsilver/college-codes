
#!/usr/bin/env python3

import os

def Apresentacao():
	print ('''
 _____ ______ _____ _____       
|_   _|  ____/ ____|  __ \      
  | | | |__ | (___ | |__) |   _ 
  | | |  __| \___ \|  ___/ | | |
 _| |_| |    ____) | |   | |_| |
|_____|_|   |_____/|_|    \__, |
                           __/ |
                          |___/   Versão: 1.2 BETA
''')

def Principal():
	Apresentacao()
	print ('''
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar;
1) Avançar;
2) Atualizar; [\033[1;91m!\033[1;m]
3) Sobre;
4) Sair;
''')
	princiaplopcao = input("\033[1;36mOpção:\033[1;m ")
	if princiaplopcao == "1":
		PrinciaplOpcao1()
	elif princiaplopcao == "2":
		ComandoNaoEncontrado()
	elif princiaplopcao == "3":
		PrincipalOpcao3()
	elif princiaplopcao == "4":
		PrincipalOpcao4()
	else:
		ComandoNaoEncontrado()

def PrinciaplOpcao1():
	print ('''
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar;
1) Ativar/Desativar Interfaces;
2) Mudança de endereço de Rede;
3) Ver Interfaces disponíveis;
4) Adicionar novas Interfaces;
5) Voltar;
''')
	princiaplopcao1 = input("\033[1;36mOpção:\033[1;m ")
	if princiaplopcao1 == "1":
		AtivarDesativarInterfaces()
	elif princiaplopcao1 == "2":
		MudancaDeEnderecoDeRede()
	elif princiaplopcao1 == "3":
		VerInterfaceDisponiveis()
	elif princiaplopcao1 == "4":
		AdicionarNovasInterfaces()
	elif princiaplopcao1 == "5":
		VoltarAoMenuPrincipal()
	else:
		ComandoNaoEncontrado()

def AdicionarNovasInterfaces():
	print ('''
[\033[1;32m*\033[1;m] Para prosseguir digite algumas informações abaixo:
[\033[1;32m*\033[1;m] Exemplo de uma Nova Interface: eth0:0
''')
	variavelnovainterfacenome = input("\033[1;36mDigite o nome da Nova Interface:\033[1;m ")
	variavelnovainterfaceip = input("\033[1;36mDigite o IP da Nova Interface:\033[1;m ")
	variavelnovainterface = "ifconfig " + variavelnovainterfacenome + " " + variavelmudancaip
	os.system(variavelnovainterface)
	print ("[\033[1;32m*\033[1;m] Nova Interface ", variavelnovainterface, ", adicionada com Sucesso!\n")
	VoltarOuSair()

def VerInterfaceDisponiveis():
	print ('''
[\033[1;32m*\033[1;m] Essas são as seguintes Interfaces disponíveis:
''')
	os.system("ifconfig -a")
	print ("\n")
	VoltarOuSair()

def MudancaDeEnderecoDeRede():
	print ('''
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar;
1) Continuar;
2) Voltar ao Menu Principal;
''')
	variavelmudancadeenderecoderede = input("\033[1;36mOpção:\033[1;m ")
	if variavelmudancadeenderecoderede == "1":
		print ('''
[\033[1;32m*\033[1;m] Para prosseguir digite algumas informações abaixo:
			''')
		variavelmudancainterface = input("\033[1;36mDigite o nome da sua interface:\033[1;m ")
		variavelmudancaip = input("\033[1;36mDigite o seu novo Endereço de IP:\033[1;m ")
		variavelmudancadeenderecodeip = "sudo ifconfig -a " + variavelmudancainterface + " " + variavelmudancaip
		os.system(variavelmudancadeenderecodeip)
	elif variavelmudancadeenderecoderede == "2":
		VoltarAoMenuPrincipal()
	else:
		ComandoNaoEncontrado()

def AtivarDesativarInterfaces():
	print ("\n")
	listarinterfaces = os.system("ifconfig")
	print ('''
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar;
1) Ativar;
2) Desativar;
3) Voltar ao Menu Principal;
''')
	varativardesativarinterfaces = input("\033[1;36mOpção:\033[1;m ")
	if varativardesativarinterfaces == "1":
		print ("\n[\033[1;32m*\033[1;m] Caso seja solicitado a senha ROOT, insira-a para proceder;")
		ativarinterface = input("[\n\033[1;32m*\033[1;m] Digite a Interface que deseja ser Ativada: ")
		variavelativarinterface = "sudo ifconfig " + ativarinterface + " up"
		os.system(variavelativarinterface)
		print ("\n[\033[1;32m!\033[1;m] Interface ativada com Sucesso!\n")
		VoltarOuSair()
	elif varativardesativarinterfaces == "2":
		print ("\n[\033[1;32m*\033[1;m] Caso seja solicitado a senha ROOT, insira-a para proceder;")
		desativarinterface = input("\n[\033[1;32m*\033[1;m] Digite a Interface que deseja ser Desativada: ")
		variaveldesativarinterface = "sudo ifconfig " + desativarinterface + " down"
		os.system(variaveldesativarinterface)
		print ("\n[\033[1;32m!\033[1;m] Interface desativada com Sucesso!\n")
		VoltarOuSair()
	elif varativardesativarinterfaces == "3":
		VoltarAoMenuPrincipal()
	else:
		ComandoNaoEncontrado()

def VoltarOuSair():
	print ('''
[\033[1;32m*\033[1;m] Escolha uma das opções abaixo para continuar;
1) Voltar ao Menu Principal;
2) Sair;
''')
	variavelvoltarousair = input("\033[1;36mOpção:\033[1;m ")
	if variavelvoltarousair ==  "1":
		VoltarAoMenuPrincipal()
	elif variavelvoltarousair == "2":
		Sair()
	else:
		ComandoNaoEncontrado()

def PrincipalOpcao3():
	print ('''
[\033[1;32m*\033[1;m] Sobre;
\033[1;36mProjeto:\033[1;m IFSPy..
\033[1;36mDesenvolvedores:\033[1;m Ygor - (M4GN4) \033[1;36me\033[1;m Thiago (S3N4)
\033[1;36mAno:\033[1;m 2016
\033[1;36mVersão Atual:\033[1;m 1.2 BETA
\033[1;36mVersão Estável:\033[1;m 1.0
\033[1;36mRequerimentos:\033[1;m GNU/Linux, Python3
\033[1;36mDescrição:\033[1;m Ferramenta auxiliar para a automatização do comando "ifconfig"; Ideal para
novos usuários no mundo GNU/Linux.
\033[1;36mCompatilidade com Distribuições:\033[1;m Arch Linux, Ubuntu/Debian
''')
	print ("\n")
	VoltarAoMenuPrincipal()

def PrincipalOpcao4():
	Sair()

def Sair():
	comandoclear = os.system("clear")
	os.system("exit")

def ComandoNaoEncontrado():
	print ('''
[\033[1;91m!\033[1;m] Desculpe, mas o comando não foi encontrado;
[\033[1;91m!\033[1;m] Caso o problema persista, relate ao desenvolvedor;
		''')
	VoltarAoMenuPrincipal()

def VoltarAoMenuPrincipal():
	input("\n\033[1;36mPressione ENTER para voltar ao Menu Principal;\033[1;m ")
	comandoclear = os.system("clear")
	Inicio()

def Inicio():
	os.system("clear")
	Principal()
Inicio()