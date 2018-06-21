import random

def main():
    linhas = input ("Linhas: ")
    colunas = input ("Colunas: ")
    
    matriz = gerar_matriz(linhas, colunas)
    
    mostrar_matriz (matriz, linhas, colunas)
       
          
    for x in range (linhas):
        print ("Maior elemento da linha %d: %d" %(x, maior_linha (matriz, linhas, colunas, x) ) )
            
            
## Funcao que gera uma matriz            
def gerar_matriz (linha, coluna):
    matriz = [ ]
    for x in range (linha):
        matriz.append([])
        for y in range (coluna): 
            matriz[x].append(random.randrange(0,10))
        
    return matriz

## Funcao que mostra a matriz
def mostrar_matriz (matriz, linha, coluna):
    for x in range (linha):
        for y in range (coluna):
            print matriz[x][y], 
        print ""
         
## Funcao retorna o maior elemento da linha         
def maior_linha (matriz, linha, coluna, index_linha):
    maior = matriz[index_linha][0]
    
    for x in range (1, coluna):
        if maior < matriz[index_linha][x]:
            maior = matriz[index_linha][x]
            
    return maior


## Funcao que gera uma lista com os maiores elementos de cada linha
def maior_cada_linha (matriz, linha, coluna):
    maiores = [ ]
    for x in range (linha):
        maior = matriz[x][0]
        for y in range (coluna):
            if maior < matriz[x][y]:
                maior = matriz[x][y]
        maiores.append(maior)
        
    return maiores
    
main()
   
      
