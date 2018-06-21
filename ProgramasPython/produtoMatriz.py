# Produto de duas matrizes

matriz1 = []
matriz2 = []
matrizprod = []
linhas1 = input("Linhas da Matriz 1: ")
colunas1 = input("Colunas da Matriz 1: ")

linhas2 = input("Linhas da Matriz 2: ")
colunas2 = input("Colunas da Matriz 2: ")

if colunas1==linhas2:
    
    print "Matriz 1 \n"
    for i in range(linhas1):
        matriz1.append([])
		matrizprod.append([])
        for x in range(colunas1):
            matriz1[i].append(input("Linha %i e Coluna %i: "%(i,x)))
    print "Matriz 2\n"
    for i in range(linhas2):
        matriz2.append([])
        for x in range(colunas2):
            matriz2[i].append(input("Linha %i e Coluna %i: "%(i,x)))


    for x in range(linhas1):
        for i in range(colunas2):
            soma=0
            for y in range(colunas1):
                soma=soma+(matriz1[x][y] * matriz2[y][i])
            matrizprod[x].append(soma)
        

    print "Produto entre a Matriz:\n%s e %s \ne %s."%(matriz1,matriz2,matrizprod)  
 

else:
    print "\n"
    print "Nao e Possivel multiplicar uma matriz %ix%i por uma matriz %ix%i."%(linhas1,colunas1,linhas2,colunas2)
    print "Tente colocar o valor da coluna da matriz 1 igual ao valor da linha da matriz 2."



