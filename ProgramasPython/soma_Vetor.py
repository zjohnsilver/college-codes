from my_Functions import functions

bolha_Decresc = functions.bolha_Decresc


def main():
    lista = [1, 3, 4, 2, 1, 5, 2]
    lista = bolha_Decresc(lista)
    ##TESTA SE UM VALOR DO VETOR E IGUAL A SOMA DE OUTROS DOIS VALORES
    for x in range(0, len(lista) - 2):
        for y in range(x + 1, len(lista) - 1):
            for z in range(y + 1, len(lista)):
                if (lista[x] == (lista[y] + lista[z])):
                    print (("%d = %d + %d" % (lista[x], lista[y], lista[z])))
                    break

main()