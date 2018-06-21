#include <stdio.h>

int dfs(int v);

int M[105][105];
int cor[105];
int e, l;



int main(){

	int x, y;
	int i, j;
	int f = 1;
	

	
	while (scanf ("%d%d", &e, &l) && (e || l)){
	
	
		// Zerando Matriz do Grafo
		for (i = 1; i <= e; i++){
			for (j = 1; j <= e; j++){
				M[i][j] = 0;
			}
		}	
	
		// Recebendo ligacoes entre os vertices
		// As chamadas arestas
		for (i = 0; i< l; i++){
		
			scanf ("%d%d", &x, &y);
		
			M[x][y] = M[y][x] = 1;
		
		}
		
		// Zerando vetor dos vertices visitados
		for (j = 1; j<= e; j++){
		
			cor[j] = 0;
			
		}
		
		dfs(1);
		
	
		int ans = 1;
	
		for (i = 1; i <= e; i ++)
			ans = ans && cor[i];
		
		
		printf ("Teste %d\n", f);
		
		if (ans){
			printf ("normal\n\n");
		}
		else{
			printf ("falha\n\n");
		}
		
		
		f++;
	
	}
	
	return 0;
}



int dfs(int v){
	int i;
	
	cor[v] = 1;
	
	for (i = 1; i <= e; i ++){
		if (M[v][i] && !cor[i]){
			dfs(i);
		}
	}	
	
	return 0;		
}



















