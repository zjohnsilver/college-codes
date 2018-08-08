#
# Feito por João Carlos em 30.06.2018
#

# Criar um algoritm O(nT) que dado um valor positivo T, e um vetor de inteiros
# positivos, dizer se existe um subconjunto que a soma é T


# Ideia, dividir ele em vários pedaços e depois voltar somando esses pedaços


def soma_T(A, T):
    n = len(A)
    soma = [[0 for x in range(T + 1)] for y in range(n + 1)]

    # Preenche a primeira linha da matriz, nos dizendo que um subconjunto
    # que contém apenas o primeiro elemento tem um valor j
    for j in range(0, T + 1):
        soma[0][j] = A[0] == j

    for i in range(1, n): # Percorre as Linhas
        for j in range(0, T + 1): # Percorre as Colunas
        	# O vetor soma recebe True se tive no vetor
        	# algum valor que seja menor que T
			# ou se ele já tiver encontrado um subconjunto
			# que somado dê esse tal valor menor que T.
            soma[i][j] = (A[i] == j) or soma[i - 1][j]

            # Essa diferença é o que não torna ele igual
            # Então quando ele vai no vetor perguntar se na
            # posição soma[i - 1][j - A[i]] tem um subconjunto
            # de tamanho i-1, cuja soma é essa diferença
            # ele ta interessado em suprir essa diferença e ficar igual
            if (j - A[i] > 0):
                soma[i][j] = soma[i][j] or soma[i - 1][j - A[i]]

    return soma[n - 1][T]


print(soma_T([2, 3, 4, 5, 6], 1))
