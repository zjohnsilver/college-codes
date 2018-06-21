# Função que recebe Linha e Coluna da Matriz e uma lista vazia, e retorna uma matriz pronta.

matriz = [ ]

m = int(input("Número de Linhas da Matriz: "))
n = int(input("Número de Colunas da Matriz: "))

def criaMatriz(m, n, matriz):
	for i in range(1,m+1):
		linha =  [ ]
		for j in range(1,n+1):
			x = int(input("Elemento %i%i : "%(i,j)))
			linha.append(x)
		
		matriz.append(linha)
		
criaMatriz(m,n,matriz)

print (matriz)

print ("\nMatriz : ")
for x in matriz:
	print (x)
	
	
	
