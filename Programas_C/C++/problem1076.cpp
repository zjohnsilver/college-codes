#include <iostream> // Biblioteca padrão do c++
#include <cmath> // ou <math.h>

using namespace std;

void dfs(int);

int G[49][49]; // Matriz do Grafo
int cor[49];   // Vetor dos vertices visitados
int V, A; 	   // Qtd. Vertices e Qtd. Arestas
int qtd_linhas; // QTD_LINHAS sem tirar o lápis do papel
 


int main(){
	int T; // Quantidade de casos de teste
	int N; // Onde o desenho deve iniciar e terminar
	
	cin >> T; // Recebendo os casos de teste
	
	while (T--){
		qtd_linhas = 0; // Contador setado como zero a cada iteracao
		cin >> N; // Recebendo onde o desenho inicia
		cin >> V >> A; // Recebendo vertices e arestas

		
		// Zerando pedaco da matriz G que sera usada
		for (int i = 0; i < V; i++){
			cor[i] = 0; //Zerando matriz dos vertices visitados
			for (int j = 0; j < V; j++){
				G[i][j] = 0; // Zerando matriz do grafo
			}
		}
		
		// Lendo as Arestas do labirinto T
		while (A--){ // Quando for zero ele quebra o laço
			int x, y; // Arestas
			
			cin >> x >> y; // Recebendo as Arestas
			
			// Neste grafo pode-se tanto ir quanto voltar
			G[x][y] = G[y][x] = 1; // Salvando para onde ele pode andar
		}
		
		dfs(N); // Chamando funcao que vai visitar os nos
		
		cout << qtd_linhas << endl; // Imprimindo resposta
				
		
	}			
		
	return 0;
}


// Funcao que visita os nos
void dfs(int v){
	cor[v] = 1; // No v visitado
	
	for (int i = 0; i < V; i++){
		if (G[v][i]){ // Posso caminhar nessa direcao?
			if (!cor[i]){ // Se o no i ainda nao foi visitado
				qtd_linhas++; // Um traço
				dfs(i); // Visita o no i
				qtd_linhas++; // Encontrou o fim e esta voltando.
			}
		}
	}
	
}

