## Programação ##

# Usando recursividade para calcular o produto dos elementos de uma lista.


def produtorio(lista):
	if len(lista) == 1:
		return lista[0]

	else:
		return lista[0] * produtorio(lista[1:])



def main():
	lista = range(5)[1:]

	print ("Produtorio de %s: %i" %(lista, produtorio(lista)))


main()