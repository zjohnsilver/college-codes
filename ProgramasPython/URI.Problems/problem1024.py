##
## *Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser 
##  deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y'
##  deve virar caractere '|' e assim sucessivamente. 
## *Na segunda passada, a linha deverá ser invertida. 
## *Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados 
##  uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.
## URI ONLINE - Problema 1024 - Strings
##
## Created by Jon on 15.06.2016
##
## Python 3


#Primeira Passada (Caracteres Maiúsc. e Minúsc. devem ser deslocados 3 posições para a direita)
def first_pass(texto):
	new = ''
	for char in texto:
		if (97<=ord(char)<=122 or 65<=ord(char)<=90):
			new += chr(ord(char) + 3)

		else:
			new += char
	return new

#Segunda Passada (Inverter a string)
def second_pass(texto):
	return texto[::-1]

#Terceira Passada (Da metade em diante da string, deslocar uma posição a esquerda)
def third_pass(texto):
	new = texto[:len(texto)//2]
	for x in range(len(texto)//2, len(texto)):
		new += chr(ord(texto[x]) -1)	
	return new

def main():
	qtd = int(input())

	for x in range(qtd):
		texto = input()

		texto = first_pass(texto)
		texto = second_pass(texto)
		texto = third_pass(texto)

		print (texto)
		
main()

