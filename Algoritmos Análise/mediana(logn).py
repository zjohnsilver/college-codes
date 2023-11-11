def mediana(vetorX, vetorY):
    n = len(vetorX) - 1

    if len(vetorX) == 1 and len(vetorY) == 1:
        return (vetorX[0] + vetorY[0]) / 2

    print(vetorX, vetorY)
    if (len(vetorX) % 2) and (len(vetorY) % 2):
        mx = vetorX[n // 2]
        my = vetorY[n // 2]

    else:
        mx = (vetorX[n // 2] + vetorX[(n // 2) + 1]) / 2
        my = (vetorY[n // 2] + vetorY[(n // 2) + 1]) / 2

    if mx == my:
        return mx

    if mx > my:
        return mediana(
            vetorX[: (len(vetorX) // 2) + 1], vetorY[len(vetorY) // 2 :]
        )

    if mx < my:
        return mediana(
            vetorX[len(vetorX) // 2 :], vetorY[: (len(vetorY) // 2)]
        )


print(mediana([1, 2, 3, 4, 20, 30], [15, 17, 30, 40, 50, 55]))
