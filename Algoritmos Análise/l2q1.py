#
# Feito por João Carlos em 28.06.18
#

import time

# Algoritmo Recursivo Puro


def Q1_RECU(n):
    if n <= 4:
        return 0
    return Q1_RECU(n // 2) + Q1_RECU(n // 2 + 1) + Q1_RECU(n // 2 + 2) + n

#   Complexidade   #
# T(n) = 3*T(n/2) + T(1)
# a = 3, b=2, c=0
# Pelo teorema Mestre...
# O(n^(log2 3))


# Algoritmo de Memorização #

def Q1_VETOR(n):
    P = [-1 for x in range(n + 1)]

    P[0] = P[1] = P[2] = P[3] = P[4] = 0

    if P[n] >= 0:
        return P[n]

    for x in range(5, n + 1):
        P[x] = P[x // 2] + P[(x // 2) + 1] + P[(x // 2) + 2] + n

    return P[n]


#   Complexidade   #
#   O(n)

count = 0

# Algoritmo de programação dinâmica #


def Q1_MEMO(n):
    P = [-1 for x in range(n + 1)]

    P[0] = P[1] = P[2] = P[3] = P[4] = 0

    return Q1_MEMO_RECU(n, P)


def Q1_MEMO_RECU(n, P):
    global count
    count += 1
    if P[n] >= 0:
        return P[n]

    P[n] = Q1_MEMO_RECU(n // 2, P) + Q1_MEMO_RECU((n // 2) + 1, P) + Q1_MEMO_RECU((n // 2) + 2, P) + n

    return P[n]

#   Complexidade    #
#   O(log n)


valor = int(input())


Q1_MEMO(valor)

print("Quantidade de chamadas de Q1 MEMO RECU: ", count)
