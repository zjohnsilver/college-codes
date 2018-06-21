##
## Receber um valor, e dizer em qual intervalo ele esta.
## URI ONLINE - Problema 1037 - Iniciante
##
## Created by Jon on 07.03.2016
##

valor = input()

if 0<=valor<=25:
    print ("Intervalo [0,25]")
elif 25<valor<=50:
    print ("Intervalo (25,50]")
elif 50<valor<=75:
    print ("Intervalo (50,75]")
elif 75<valor<=100:
    print ("Intervalo (75,100]")
else:
    print ("Fora de intervalo")
