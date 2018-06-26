#
# Feito por João Carlos em 26.06.18
#

# ORDENA EM ORDEM CRESCENTE #

vetor = [5, 7, 2, 1, 9]


def QuickSort(vetor, p, r):
    if p < r:
        q = Particione(vetor, p, r)
        QuickSort(vetor, p, q - 1)
        QuickSort(vetor, q + 1, r)

    return vetor


def Particione(vetor, p, r):
    pivo = vetor[r]
    i = p - 1

    print("Antes: ", vetor)

    for j in range(p, r):
        if vetor[j] < pivo:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]

    vetor[i + 1], vetor[r] = vetor[r], vetor[i + 1]

    print("Depois", vetor)

    print("\n")

    return i + 1


print("Final:", QuickSort(vetor, 0, len(vetor) - 1))
