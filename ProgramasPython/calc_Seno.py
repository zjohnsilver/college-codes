from my_Functions import functions

fat = functions.fatorial


def main():
    seno = 0
    x = input("Numero:\n>> ")

    for n in range(21):
        seno += float(((-1) ** n) * (x ** ((2 * n) + 1))) / fat(2 * n + 1)

    print (("Seno: %.2f" % (seno)))


main()