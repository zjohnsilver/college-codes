"""
12) Faca um programa para receber a quantidade de elementos de duas listas e os elementos de cada
uma. O programa deve mostrar os elementos que estao na intersecao das duas listas.
"""

lista1 = [ ]
lista2 = [ ]

qtd1 = input("Qtd elementos lista 1: ")

qtd2 = input("Qtd elementos lista 2: ")

for x in range(qtd1):
	lista1.append(input("Numero lista 1: "))

for i in range(qtd2):
	lista2.append(input("Numero lista 2: "))
	
intersecao = [ ]
for x in range(qtd1):
	y=lista1[x]
	for i in range(qtd2):
		if y==lista2[i]:
			intersecao.append(y)

			
print intersecao



#Lancelot
			