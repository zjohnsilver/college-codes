lista = [1, 3, 4, 2, 1, 5, 2]
pares_Iguais = 0

##Usando ordenacao bolha para testar valor com valor
for x in range(0, len(lista) - 1):
    for y in range(x + 1, len(lista)):
        if (lista[x] == lista[y]):
            pares_Iguais += 1
            break

print (("Numero de Pares Iguais no vetor %s:" % (lista)))
print ((">> %d pares iguais" % (pares_Iguais)))