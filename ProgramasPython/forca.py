import random

palavras = "formiga abacaxi cama carnaval cachorro cavalo ".split()

def geraPalavraAleatoria():
	global palavras
	return random.choice(palavras)
	
def imprimeComEspacos(palavra):
	for letra in palavra:
		print (letra, end=" ")
		print( )
		
#Vídeo 49 de python ( Ignorância Zero)