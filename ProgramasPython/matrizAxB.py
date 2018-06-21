#Matriz de Qualquer Tamanho:

matriz = []

Linhas = input("Linhas: ")
Colunas = input("Colunas: ")

for x in range(Linhas):
	matriz.append([])
	for i in range(Colunas):
		matriz[x].append(input("Linha %i e Coluna %i: "%(x,i)))



print "\n",matriz