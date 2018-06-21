lista = [3, 1, 3, 2, 5]

exist = False

for x in range(0, len(lista) - 1):
    for y in range(x + 1, len(lista)):
        if (lista[x] == lista[y]):
            exist = True

if (exist):
    print ("Ha elementos repetidos.")
else:
    print ("Nao ha elementos repetidos.")