#
# Feito por João Carlos em 30/06/18
#

# Algoritmo Recursivo que busca a maior subsequencia crescente dentro de um vetor

# n é a posição final


def SSC_maxima(A, n):
    c = 1

    # para i = n-1 ... 0
    for i in range(n - 1, -1, -1):
        if A[i] <= A[n]:
            d = SSC_maxima(A, i)

            if d + 1 > c:
                c = d + 1
    return c


print(SSC_maxima([9, 5, 6, 3, 9, 6, 4, 7], 7))
