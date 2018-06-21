#include <iostream>
#include <string.h>

using namespace std;

int dfs(int v);

int G[20][20];
int cor[20];
int V, E;
int lvl;
int teste = 0;

int main(){
	int qtd_testes;
	int count = 1;
	
	cin >> qtd_testes;
	
	while (qtd_testes--){
		// Zerando vetores G e Cor
		memset(G, 0, sizeof(G));
		memset(cor, 0, sizeof(cor));

		cout << "Caso " << count++ << ":" << endl;
	
		cin >> V >> E;
		
		for (int i = 0; i < E; i++){
			int x, y;
			cin >> x >> y;
			
			G[x][y] = 1;
			
		}
		
		for (int j = 0; j < V; j++){
			lvl = 0;
			dfs(j);
			// Essa variavel verifica se ele esta indo
			// para outra parte do grafo, outro vertice
			if (teste){
				cout << endl;
				teste = 0;
			}
		}
	
	}
		
	return 0;
}


int dfs (int v){
	cor[v] = 1;
	lvl++; // Para saber em qual lvl ele está no grafo
	for (int i = 0; i < V; i++){
		if (G[v][i]){
			if (!cor[i]){
				teste = 1;
				for (int j = 0; j < lvl; j++)
					cout << "  ";
				cout << v << "-" << i 
					<< " pathR(G," << i << ")"<< endl;
				dfs(i);
				lvl--;
			}
			else{
				if (teste){
					for (int j = 0; j < lvl; j++)
						cout << "  ";
					cout << v << "-" << i << endl;}	
					
			}
		}
	}
	
	return 0;
}
