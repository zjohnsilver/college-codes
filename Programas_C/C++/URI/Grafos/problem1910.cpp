#include <iostream>
#include <cstdlib>
#include <queue>
#include <utility>

using namespace std;

int dist[100000];
int cor[100000];
int caso;

int bfs(int inicio, int fim);
int O, D, K;

int main(){
	caso = 1;	
	while (cin >> O >> D >> K && (O || D || K)){
			
		for (int i = 0; i < K; i++){
			int c;
			cin >> c;
			cor[c] = caso;
		}

		cout << bfs(O, D) << endl;			
		
		caso++;
	}
   
    return 0;
}

int bfs(int inicio, int fim){
	cor[inicio] = caso;
    dist[inicio] = 0;
   
    queue <int> fila; // cria a fila
   
    fila.push(inicio); //adiciona inicial a fila 

	//Operacoes: +1, -1, /2, x2, x3
	while (fila.size()){
		int atual = fila.front();
		fila.pop();

		if (atual == fim){
			return dist[fim];
		}	
		// Vetor das operações que podem ser feitas
		int operacoes[] = {atual+1, atual-1, (atual%2 == 0)?atual/2:-1, atual * 2, atual*3};
		
		for (int i = 0; i < 5; i++){
			int valor = operacoes[i];

			if (valor <= 0 || valor > 100000) continue;			
			if (cor[valor] != caso){
				cor[valor] = caso;
				dist[valor] = dist[atual]+1;
				fila.push(valor);
			}	
		}
	}
	
	return -1;
}
