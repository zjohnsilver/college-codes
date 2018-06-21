### Sistemas Operacionais ###
### Deteccao de Impasses  ###
 
# Variaveis globais
 
             #Grafo
G = []
         
visitados = [0, 0, 0, 0, 0, 0] # vetor de visitados
N = 6 # Total de vertices
impasse = False
qtd_P = qtd_R = 0
def leitura():
	global G
	arq = open("dados.txt", "r")
	qtd_P, qtd_R = arq.readline().split()
	qtd_P = int(qtd_P)
	qtd_R = int(qtd_R)
	G = [[0 for x in range(qtd_P+qtd_R)] for x in range(qtd_P + qtd_R)]
	r = arq.read().split("\n")
	arq.close()	
	for linha in r:
		if linha:
			if (linha[0] == 'P'):
				linhaP = int(linha[1])
				linha = linha.split()[1:] ## [0, 1, 0]
				for index in range(len(linha)):
					if int(linha[index]):
						G[linhaP][qtd_P + index] = 1
			if (linha[0] == "R"):
				linhaR = int(linha[1])
				linha = linha.split()[1:] ## [0, 1, 0]
				for index in range(len(linha)):
					if int(linha[index]):
						G[qtd_P+linhaR][index] = 1

def dfs(v):
    global impasse
    if (not impasse):
        visitados[v] = 1

        for x in range (0, N):
            if (G[v][x]):
                if (not visitados[x]):
                    dfs(x)
                else:
                    impasse = True
     
 
 
def main():
	"""
     global impasse
     ## Grafo Pagina 273 do livro
     dfs(0)
     if (impasse):
         print "Impasse"
     else:
         print "Nao tem Impasse"
	"""
	leitura()
	print G     
 
 
main()
