#include <iostream>
#include <cstdlib>

using namespace std;

int G[1050][1050];
int x;
int n, m;

int dl[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

void dfs(int l, int c);

int limite(int l, int c) {
	return l>=0 && l < n && c>=0 && c < m;
}

int main(){
	cin >> n >> m;
	
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			char c;
			cin >> c;
			if (c == 'o'){
				G[i][j] = 1;
			}
			else if (c == '.'){
				G[i][j] = 0;
			}
		}
	}
	
	int ans = 0;
	
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			if (!G[i][j]){
				dfs(i, j);
				ans++;
			}
		}
	}
	
	cout <<  ans << endl;
	
	return 0;
}

void dfs(int l, int c){
	G[l][c] = 1;
	
	for (int i=0; i < 4; i++){
		if (limite(l + dl[i], c + dc[i]) &&
				G[l+dl[i]][c+dc[i]] == 0){
			dfs(l+dl[i], c+dc[i]);			
		}
	}	
}
