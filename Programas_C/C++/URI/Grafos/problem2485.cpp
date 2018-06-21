#include <iostream>
#include <cstdlib>
#include <queue> // Necessário para a fila
#include <utility> // Necessário para o pair

using namespace std;

int G[105][105]; // Matriz do grafo
int dist[105][105]; // Matriz da distância de todas as casas da matriz
int l[] = {0, 0, 1, 1, 1, -1, -1, -1}; // Andar na linha
int c[] = {1, -1, 0, 1, -1, 0, 1, -1}; // Andar na coluna
int A, B; // Quantidade de linhas e colunas da matriz
int X, Y; // Coordenadas de onde o antidoto será aplicado

int bfs(int inicio, int fim);
int limite(int l, int c);

int main(){
    int qtd_casos;
    
    cin >> qtd_casos;
    
    while (qtd_casos--){
		//Dimensões do grafo
        cin >> A >> B;
        // Recebe o Grafo
        for (int i = 1; i <= A; i++){
            for (int j = 1; j <= B; j++){
                cin >> G[i][j];
            }
        }

        cin >> X >> Y; // Recebe as coordenadas de onde ele vai injetar o antidoto
        
        cout << bfs(X, Y) << endl; // Chama a bfs
    }

    return 0;
}

// Busca em largura usando fila
int bfs(int inicio, int fim){
	// Dando "distância" infinita para todos os outros
    for (int i = 1; i <= A; i++){
        for (int j = 1; j<=B; j++){
            dist[i][j] = 100000;
        }
    }
    dist[inicio][fim] = 0; // A distância do primeiro e zero
    
    queue <pair<int, int> > fila; // cria a fila
    
    fila.push(make_pair(inicio, fim)); //adiciona inicial a fila
    int maior = 0;
    
    //Enquanto houver elementos na fila
    while (fila.size()){
        int x = fila.front().first; // Primeiro elemento da fila
        int y = fila.front().second; // Segundo elemento da fila
        fila.pop(); // retira da fila
        for (int i = 0; i < 8; i++){ // Esse for vai percorrer os vetores l e c, que são a função janela
            int xx = x + l[i];
            int yy = y + c[i];
            
            // Se tiver dentro do limite, se a distância atual for maior do que a distancia anterior + 1
            // E se o nó estiver infectado (G[xx][yy] = 1) então entra
            if (limite(xx, yy) && (dist[xx][yy]>dist[x][y] + 1) && G[xx][yy]){
                dist[xx][yy] = dist[x][y] + 1; // Incrementa um na distância, pois alcançou este nó
                maior = max(maior, dist[xx][yy]); // Salva em maior o valor da maior distância
                fila.push(make_pair(xx, yy)); // Adiciona esse novo par a fila, para alcançar os seguintes
            }
        }
    }
    
    return maior; // Retorna a maior distância que foi percorrida
}

// Essa função vai testar se ele ainda está dentro dos limites da matriz G
int limite(int l, int c){
    return l>=1 && l<=A && c>=1 && c<=B;
}
