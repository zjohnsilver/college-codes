### Sistemas Operacionais ###
### Deteccao de Impasses  ###

# Variaveis globais

	         #Grafo
     ### P0  P1 P2 R0 R1 R2
G = [#P0 [0, 0, 0, 0, 1, 0],
	 #P1 [0, 0, 0, 0, 0, 1],
	 #P2 [0, 0, 0, 1, 0, 0],
	 #R0 [1, 0, 0, 0, 0, 0],
	 #R1 [0, 1, 0, 0, 0, 0],
	 #R2 [0, 0, 1, 0, 0, 0]] 
		
visitados = [0, 0, 0, 0, 0, 0] # vetor de visitados
N = 6 # Total de vertices
impasse = False

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
	global impasse
	## Grafo Pagina 273 do livro
	dfs(0)
	if (impasse):
		print "Impasse"
	else:
		print "Nao tem Impasse"
	


main()
