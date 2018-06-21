#include <iostream>
#include <cstring>

void dfs(int);
int verifica_visitados();

using namespace std;

int G[101][101];
int cor[101];
int N, M;

int main(){
	int T;
	int f = 1;
	
	cin >> T;
	while (T--){
		cin >> N; // Pontos principais da cidade
		cin >> M; // N° estradas já construídas
		
		memset(G, 0, sizeof(G));
		memset(cor, 0, sizeof(cor));
		
		for (int i = 0; i < M; i++){
			int x, y;
			cin >> x >> y;
			G[x][y] = G[y][x] = 1;
		}
		
		int count = 0;
		for (int i = 1; i <= N; i++){
			if (!verifica_visitados()){
				if (!cor[i]){
					count++;
					dfs(i);
				}
			}
		}
		
		if (count == 1) 
			cout << "Caso #" << f << 
				": a promessa foi cumprida" << endl;
		else
			cout << "Caso #" << f <<
				": ainda falta(m) " << count-1 <<
					" estrada(s)" << endl;
			
		f++;
	}
	
	
	return 0;
}

void dfs(int v){
	cor[v] = 1;
	
	for (int i = 1; i <= N; i++){
		if (G[v][i]){
			if (!cor[i]){
				dfs(i);
			}
		}	
	}
}

int verifica_visitados(){
	int ans = 1;
	
	for (int j = 1; j <= N; j++){
		ans = ans & cor[j];
	}
	
	return ans;
}
