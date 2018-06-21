##
## Entrada com 3 valores, aplicar Bhaskara, informar as 2 raizes
## Dizer se for impossivel calcular. Ex: A=0 ou b² - 4ac < 0
## URI ONLINE - Problema 1036 - Iniciante
##
## Created by Jon on 07.03.2016
##

string = raw_input().split() ## 3 valores seram recebidos em linha. Por isso o split.

A = float(string[0])
B = float(string[1])
C = float(string[2])
if (B**2 - 4*A*C)<0 or A==0:
    print ("Impossivel calcular")
else:
    raiz1 =(-B + (B**2 - 4*A*C)**0.5)/(2*A)
    raiz2 =(-B - (B**2 - 4*A*C)**0.5)/(2*A)
    print ("R1 = %.5f"%(raiz1))
    print ("R2 = %.5f"%(raiz2))



