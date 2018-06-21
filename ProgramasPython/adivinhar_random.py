from random import randint

print ("ADIVINHE O NÚMERO")

print ("MENU:")

print ("""1 - Facil\n2 - Médio\n3 - Difícil""")

print ("")

dificuldade = int(input("Dificuldade: "))

print ("")

TAM_INTERVALO = 50

adivinhar = randint(1,TAM_INTERVALO)





"""

    PROGRAMA NÃO ESTÁ CONSIDERANDO O CHUTE QUE EU DOU NA TOMADA DE DECISÃO

"""



while True:
    chute = int(input("Dê um chute: "))

    print ("")

    intervalo1 = [x for x in range(0, adivinhar-1)]
    intervalo2 = [x for x in range(adivinhar+1, TAM_INTERVALO+1)]
    
    if dificuldade == 3:
        if chute in intervalo1:
            print ("\tChute mais alto")
        elif chute in intervalo2:
            print ("\tChute mais baixo")
        else:
            print ("\tVocê acertou")
            break
    
    elif dificuldade == 2:
        sub_intervalo1 = intervalo1[:len(intervalo1)//2]
        sub_intervalo2 = intervalo1[len(intervalo1)//2:]

        sub_intervalo3 = intervalo2[:len(intervalo1)//2]
        sub_intervalo4 = intervalo2[len(intervalo1)//2:]

        if chute in sub_intervalo1:
            print ("\tChute bem mais alto")
                                    
        elif chute in sub_intervalo2:
            print ("\tChute mais alto")
                                    
        elif chute in sub_intervalo3:
            print ("\tChute mais baixo")
                                    
        elif chute in sub_intervalo4:
            print ("\tChute bem mais baixo")

        else:
            print ("\tVocê acertou")
            break


    elif dificuldade == 1:
        tam_quadrante = len(intervalo1)//3
        tam_quadrante2 = len(intervalo2)//3
        
        sub_intervalo1 = intervalo1[:tam_quadrante]
        sub_intervalo2 = intervalo1[tam_quadrante:2*(tam_quadrante)]
        sub_intervalo3 = intervalo1[2*(tam_quadrante):]

        sub_intervalo4 = intervalo2[:tam_quadrante2]
        sub_intervalo5 = intervalo2[tam_quadrante2:2*(tam_quadrante2)]
        sub_intervalo6 = intervalo2[2*(tam_quadrante2):]


        if chute in sub_intervalo1:
            print ("\tChute bem mais alto")

        elif chute in sub_intervalo2:
            print ("\tChute mais alto")

        elif chute in sub_intervalo3:
            print ("\tChute um pouco mais alto")

        elif chute in sub_intervalo4:
            print ("\tChute um pouco mais baixo")

        elif chute in sub_intervalo5:
            print ("\tChute mais baixo")

        elif chute in sub_intervalo6:
            print ("\tChute bem mais baixo")

        else:
            print ("\tVocê ganhou")
            break
    
    print ()

    
