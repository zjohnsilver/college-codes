continuar = True
while continuar:
    print ("--------------------------------------------------------------")
    print ("""\t\t\tCALCULA DEZENAS """)
    print ("""\t\t\t---------------""")

    print ()

    print ("""DESCRIÇÃO: Informa quantas dezenas há em um número qualquer.""")
    print ()
    print ("""SAIR: Digite S, s ou sair""")
    print ("--------------------------------------------------------------")
    print ("\n")

    while True:
        numero = input("Digite um número: ")
        try:
            numero = abs(float(numero))
            break
        except ValueError:
            if numero in ['s', 'S', 'sair']:
                continuar = False
                break
            print ("\nValor invalido, por favor digite apenas números")
        finally:
            print ("\n")

    if not continuar:
        break

    aux = numero

    qtd_dezenas = 0
    while numero >= 10:
        qtd_dezenas +=1
        numero -=10

    saida = "SAIDA: "
    saida += str(aux) + " tem " + str(qtd_dezenas) + " dezena"

    if qtd_dezenas >1:
        saida += "s"

    print (saida)


print ("FIM DO PROGRAMA")
