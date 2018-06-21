def bolha_Cresc(lista):
    for x in range(0, len(lista) - 1):
        for y in range(x + 1, len(lista)):
            if (lista[x] > lista[y]):
                lista[x] = lista[x] ^ lista[y]
                lista[y] = lista[x] ^ lista[y]
                lista[x] = lista[x] ^ lista[y]

    return lista
	
def bolha_Decresc(lista):
    for x in range(0, len(lista) - 1):
        for y in range(x + 1, len(lista)):
            if (lista[x] < lista[y]):
                lista[x] = lista[x] ^ lista[y]
                lista[y] = lista[x] ^ lista[y]
                lista[x] = lista[x] ^ lista[y]

    return lista
	
def fatorial(x):
	fat = 1
	for y in range(1, x+1):
		fat = fat*y
		
	return fat
