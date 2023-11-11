#
# Feito por João Carlos em 01.07.18
#


def festa(lista_amigos, lista_pares_conhecidos):
    matriz_conhecidos = [
        [0 for x in range(max(lista_amigos) + 1)] for y in range(max(lista_amigos) + 1)
    ]

    for amigo in lista_amigos:
        for par in lista_pares_conhecidos:
            pessoa1 = par[0]
            pessoa2 = par[1]

            if amigo == pessoa1:
                matriz_conhecidos[amigo][pessoa2] = 1
            elif amigo == pessoa2:
                matriz_conhecidos[amigo][pessoa1] = 1

    return matriz_conhecidos


def print_matriz(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            print(matriz[linha][coluna], end="  ")
        print("\n")


print_matriz(
    festa(
        [3, 4, 1, 2, 6, 7, 8, 0, 12, 13, 11, 10],
        [(3, 4), (3, 1), (3, 8), (3, 2), (3, 12), (3, 13), (3, 11)],
    )
)
