def main():
    print ("PROGRAMA CARACTER QUE MAIS SE REPETE:\n")

    word = raw_input("Palavra: ")
    lista2 = char_Repeat(word)
    if (lista2[0] != 0):
        print ("O caracter ((%s)) se repete %d vezes" % (lista2[0], lista2[1]))
    else:
        print ("Nao a caracter repetido na string.")


def char_Repeat(string):
    lista = [0, 0]
    geral = 0
    for x in range(0, len(string) - 1):
        cont = 0
        for y in range(x + 1, len(string)):
            if (string[x] == string[y]):
                cont += 1
        if (cont > geral):
            geral = cont
            lista[0] = (string[x])
            lista[1] = (cont)

    return lista

main()