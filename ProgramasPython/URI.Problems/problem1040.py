## 
## Leia 4 notas (N1,N2,N3,N4), e calcule a media com pesos 2, 3, 4 e 1 respectivamente
## URI ONLINE - Problema 1040 - Iniciante
##
## Created by Jon on 07.03.2016
##

string = raw_input().split() ## Recebe quatro valores

N1 = float(string[0])
N2 = float(string[1])
N3 = float(string[2])
N4 = float(string[3])

media = (N1*2 + N2*3 + N3*4 + N4*1)/10.0 ## Media ponderada. Pesos: (2, 3, 4, 1)

print ("Media: %.1f"%(media))

if media >= 7.0:
    print ("Aluno aprovado.")
elif media < 5.0:
    print ("Aluno reprovado.")
else:
    print ("Aluno em exame.")
    exame = input()
    print ("Nota do exame: %.1f"%(exame))
    
    media = (media + exame)/2.0 ## Reaproveitei a variavel media.
    
    if media>=5.0:
        print ("Aluno aprovado.")
    else:
        print ("Aluno reprovado.")
    print ("Media final: %.1f" %(media))
    
