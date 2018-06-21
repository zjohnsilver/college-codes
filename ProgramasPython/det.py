from random import randrange

def criar_matriz (ordem):
	matriz = []	
	for x in range(ordem):
		matriz.append([])
		for y in range(ordem):
			matriz[x].append (randrange(0,10))

	return matriz


def mostrar_matriz (matriz, ordem):

	for x in range(ordem):
		for y in range(ordem):
			print "\t",matriz[x][y]," ",
		
		print "\n"


## Funcao que faz uma matriz segundo o teorema de LAPLACE
def sobra_matriz (matriz, linha_eliminar, ordem): # A coluna a ser eliminada, sera sempre a primeira
	matriz_sobra = [] 
	k=0;
	for x in range(ordem-1):
		matriz_sobra.append([])

	for x in range(0, ordem):
		for y in range(1, ordem):
			if x!=linha_eliminar:
				matriz_sobra[k].append(matriz[x][y])

		if x!=linha_eliminar:
			k+=1
	return matriz_sobra


## DETERMINANTE PELO METODO DE LAPLACE
def determinante (matriz, ordem):
	if (ordem == 2):
		return (matriz[0][0]*matriz[1][1] - (matriz[0][1]*matriz[1][0]))

	det = 0
	lista = []
	
	for x in range(ordem): ##Laco para percorrer a 1 coluna
		lista.append(matriz[x][0])

	for x in range(len(lista)):		
		det+= lista[x]*((-1)**(x+2))*determinante(sobra_matriz(matriz, x, ordem), ordem-1)  

	return det	

def main():

	ordem = input("\nOrdem da Matriz: ")

	print ("\n")
	
	matriz = []
	"""
	USAR ISSO QUANDO EU QUISER ATUALIZAR O USUARIO COM A MATRIZ.

	for x in range(ordem):
		matriz.append([])
		for y in range(ordem):
			matriz[x].append(0)
	for x in range(ordem):
		for y in range(ordem):
			matriz[x][y]=(input("Elemento a%i%i: "%(x+1,y+1)))
			if x!=ordem-1 or y!=ordem-1:
				mostrar_matriz (matriz, ordem)
	"""

	##Pede os elementos da matriz ao usuario
	for x in range(ordem):
		matriz.append([])
		for y in range(ordem):
			matriz[x].append(input("Elemento a%i%i: " %(x+1, y+1)))

	##matriz = criar_matriz(ordem)

	print ("\n")

	print ("MATRIZ A: ")
	mostrar_matriz (matriz, ordem)

	print ("Det(A) =  %i\n" %(determinante (matriz, ordem)));


main()
			
