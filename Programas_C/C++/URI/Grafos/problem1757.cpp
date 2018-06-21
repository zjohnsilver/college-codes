#include <iostream>
#include <cstring>

void dfs(int);

using namespace std;

int G[100][100];
int cor[100];
int N, V;

int main(){
	int T;
	
	cin >> T; // Quantidade de casos de teste
	while (T--){
		memset (G, 0, sizeof(G));
		memset (cor, 0, sizeof(cor));
		
		cin >> N >> V;
		
		for (int i = 0; i < V; i++){
			int A, B;
			
			cin >> A >> B;
			
			G[A][B] = 1;

		}
		
		dfs(0);
		int ans = 1;
		
		for (int i = 0; i < N; i++){
			ans = ans & cor[i];
		}
		
		if (ans) 
			cout << "1" << endl;
		else
			cout << "0"<< endl;
	}



	return 0;
}

void dfs(int v){
	cor[v] = 1;
	
	for (int i = 0; i < N; i++){
		if (G[v][i]){
			if (!cor[i]){
				cor[i] = 1;
			}
		}	
	}
}


