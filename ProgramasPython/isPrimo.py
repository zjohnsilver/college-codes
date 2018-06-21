
def isPrimo(p):
    qtd_divisores = 0

    for x in range(2, p):
        if p % x == 0:
            qtd_divisores += 1
    if qtd_divisores == 0:
        return 1

    return 0


def primos():
    for n in range(1, 100):
        if isPrimo(n):
            for x in range(0, 51, 12):
                if isPrimo(n + x):
                    print(n, "+", x, "é", isPrimo(n + x))


primos()
