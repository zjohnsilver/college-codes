def esquerda90(lista, linhas, colunas):
    k = 0
    matriz = []
    for i in range(linhas):
        matriz.append([])
    for i in range(linhas):
        for j in range(colunas):
            matriz[i].append(0)

    for j in range(colunas):
        for i in range(linhas-1,-1,-1):
            matriz[i][j] = lista[k]
            k += 1
    return matriz

def direita90(lista, linhas, colunas):
    k = 0
    matriz = []
    for i in range(linhas):
        matriz.append([])
    for i in range(linhas):
        for j in range(colunas):
            matriz[i].append(0)

    for j in range(colunas-1, -1, -1):
        for i in range(linhas):
            matriz[i][j] = lista[k]
            k += 1
    return matriz

def espelhar(lista, linhas, colunas):
    k = 0
    matriz = []
    for i in range(linhas):
        matriz.append([])
    for i in range(linhas):
        for j in range(colunas):
            matriz[i].append(0)

    for i in range(linhas):
        for j in range(colunas-1,-1,-1):
            matriz[i][j] = lista[k]
            k += 1
    return matriz

def inverterOrdem(matriz):
    aux = ordem[1]
    ordem[1] = ordem[0]
    ordem[0] = aux
    return ordem

def matrizLista(matriz):
    lista = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            lista.append(matriz[i][j])
    return lista

s = raw_input('Digite o nome da imagem que voce quer manipular:')
arq = open(s, 'r')

informacoes = []
for i in range(4):
    informacoes.append(arq.readline())

ordem = informacoes[2].split()
colunas = int(ordem[0])
linhas = int(ordem[1])

listaString = arq.read()
lista = listaString.split()
arq.close()

matriz = []
opcao = -1
while opcao != 0:
    opcao = input('Digite a opcao desejada:\n1-Virar a imagem 90 graus para esquerda\n2-Virar a imagem 90 graus para direita\n3-Espelhar a imagem\n0-Salvar a imagem\n')
    if opcao == 1:
        inverterOrdem(ordem)
        colunas = int(ordem[0])
        linhas = int(ordem[1])
        informacoes[2] = str(colunas) + ' ' + str(linhas) + '\n'
        if matriz != []:
            matriz = esquerda90(matrizLista(matriz), linhas, colunas)
        else:
            matriz = esquerda90(lista, linhas, colunas)
            
    elif opcao == 2:
        inverterOrdem(ordem)
        colunas = int(ordem[0])
        linhas = int(ordem[1])
        informacoes[2] = str(colunas) + ' ' + str(linhas) + '\n'
        if matriz != []:
            matriz = direita90(matrizLista(matriz), linhas, colunas)
        else:
            matriz = direita90(lista, linhas, colunas)
            
    elif opcao == 3:
        if matriz != []:
            matriz = espelhar(matrizLista(matriz), linhas, colunas)
        else:
            matriz = espelhar(lista, linhas, colunas)
        
    elif opcao == 0:
        arq = open(s, 'w')
        for i in range(len(informacoes)):
            arq.write(informacoes[i])

        for i in range(linhas):
            s = ''
            for j in range(colunas):
                s += str(matriz[i][j])
                if j != colunas-1:
                    s += ' '
                else:
                    s += '\n'
            arq.write(s)
        arq.close()
