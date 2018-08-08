#
# Feito por João Carlos em 28.06.2018
#

# Fibonacci Memorização #


# 1 1 2 3 5 8 13 21


# Memorização

import time

# Fibonacci Clássico


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Fibonacci com Memorização

def fib_memo(posicao):
    memo = [-1 for x in range(posicao + 1)]

    memo[0] = 1
    memo[1] = 1

    for x in range(2, posicao):
        memo[x] = memo[x - 1] + memo[x - 2]

    return memo[posicao - 1]

# Recursão + Memorização


def fib_exe(posicao):
    memo = [-1 for x in range(posicao + 1)]

    memo[1] = 1
    memo[2] = 1

    return fib_recu_memo(posicao, memo)


def fib_recu_memo(posicao, memo):
    if memo[posicao] >= 0:
        return memo[posicao]
    else:
        memo[posicao] = fib_recu_memo(posicao - 1, memo) + fib_recu_memo(posicao - 2, memo)
        return memo[posicao]


valor = int(input("Valor: "))

# # # Clássico
# inicio = time.time()
# fibonacci(valor)
# fim = time.time()
# time_classico = fim - inicio

# Fib Memorização
inicio = time.time()
fib_memo(valor)
fim = time.time()
time_memo = fim - inicio

# Fib Recursão e Memorização
inicio = time.time()
fib_exe(valor)
fim = time.time()
time_recu_memo = fim - inicio

print("#### RESULTADOS ####")
print("Entrada:", valor)
# print("Fib-Clássico: %.10f" % (time_classico))
print("Fib-Memo: %.10f" % (time_memo))
print("Fib-Recu-Memo:%.10f" % (time_recu_memo))
