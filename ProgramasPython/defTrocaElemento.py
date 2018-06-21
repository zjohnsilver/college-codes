# Escreva uma função que troca elementos de uma matriz

elemento1 = int(input("Posição do elemento 1: "))
elemento2 = int(input("Posição do elemento 2: "))


def trocaElemento(pos1,pos2,matriz):
	elemento1 = matriz[pos1//10 -1][pos1%10 -1]
	elemento2 = matriz[pos2//10 -1][pos2%10 -1]
	
	matriz[pos1//10 -1][pos1%10 -1] = elemento2
	matriz[pos2//10 -1][pos2%10 -1] = elemento1
	

matriz = [] # Matriz não definida ainda
trocaElemento(elemento1,elemento2,matriz)


print (matriz)


# Conferir se estou digitando valores dentro do intervalo da matriz


# Pedir que o usuário digite a posições dos elementos novamente, caso nenhum dos dois seja "VAZIO"