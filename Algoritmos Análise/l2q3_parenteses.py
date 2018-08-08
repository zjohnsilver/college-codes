#
# Feito por João Carlos em 30.06.18
#


# Algoritmo para colocar parênteses em uma expressão
# de maneira que seu valor seja minimo

# (vetor_variaveis, operadores, qtd_variaveis)
def alg03(X, OP, n):
    v_min = [[0 for x in range(n + 1)] for x in range(n + 1)]
    s = [[0 for x in range(n + 1)] for x in range(n + 1)]
    for i in range(0, n):
        v_min[i][i] = X[i]
    for l in range(2, n + 1):
        for i in range(0, n - l + 1):
            j = i + l - 1
            v_min[i][j] = 100000
            print(i, n)
            for k in range(i, j - 1):
                print("entrei")
                m = eval(str(v_min[i][k]) + str(OP[k]) + str(v_min[k + 1][j]))
                print(m)
                if m < v_min[i][j]:
                    v_min[i][j] = m
                    s[i][j] = k
    return v_min[0][n]


print(alg03([5, 2, 1, 4], ["+", "+", "+"], 4))
