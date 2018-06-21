def main():
    print ("PROGRAMA DO PALINDROMO : ")
    word = raw_input("Palavra: ")
    palindromo(word)


def palindromo(string):
    l = len(string) - 1
    cont = 0

    for x in range(len(string) / 2):
        if (string[x] == string[l]):
            cont += 1
        l -= 1

    if (cont == len(string) / 2):
        print ("E palindromo")
    else:
        print ("Nao e palindromo")

main()
