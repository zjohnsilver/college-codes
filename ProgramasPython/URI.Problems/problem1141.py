##
## Fazenda de strings
##  
## URI ONLINE - Problema 1141 - Strings
##
## Created by Jon on 15.06.2016
## Atualizado by Lancelot on 18.05.2017
##
## Python 3


def main():
	qtd = input() ## Quantidade de palavras a ser lida
	
	### Lendo palavras da sequencia
	while qtd != 0:
		sequencia = []
		for i in range (qtd):
			sequencia.append(ler_palavra()) ## Adicionando as palavras na lista sequencia
		
		sequencia.sort(key = lambda x: len(x)) ## Organizando a lista pelo tamanho da string
		
		print sequencia
		
		qtd = input()  ## Quantidade de palavras a ser lida
	
		


def ler_palavra():
	return raw_input()	

main()
