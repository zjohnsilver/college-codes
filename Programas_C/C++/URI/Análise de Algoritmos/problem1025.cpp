#include <iostream>
#include <cstring>

using namespace std;

int lista[1000000];

int maior(int vetor[], int tam);


void ordenar(int);
int PesquisaBinaria(int, int);

int main(){
    int N, Q;
    int caso = 1;
    
    cin >> N >> Q;
    int teste = 0;

    while ((N != 0 || Q != 0) && teste < 64){
        cout << "CASE# " << caso << ":" << endl;
        int x = 0;
        while (x < N){
            int y;
            cin >> y;
            lista[x] = y;
            x++;
        }
        
        ordenar(N);
        
        x = 0;
        while (x < Q){
            int y;
            cin >> y;
            
            int retorno = PesquisaBinaria(y, N);
            
            if (retorno < 0){
                cout << y << " not found" << endl;
            }
            else{
                cout << y << " found at " << retorno << endl;
            }
            
            x++;
        }
    
        cin >> N >> Q;
        caso ++;
        teste++;
    }


    return 0;
}   


void ordenar(int tam){
    int MAXv = maior(lista, tam);

    int quantidade[MAXv + 1];
    for (int i = 0; i< MAXv + 1; i++){
        quantidade[i]  = 0;
    }

    for (int i = 0; i < tam; i++){
	    quantidade[lista[i]]++;
    }

    int i = 0;

    for (int j = 0; j < MAXv + 1; j++){
	    while (quantidade[j]){
		    lista[i++] = j;
		    quantidade[j]--;
	    }
    }
}


       

int PesquisaBinaria (int valor, int tam){
    int inf = 0;
    int sup = tam-1;
    int meio;

    while (inf <= sup){
        meio = (inf + sup)/2;
        if (valor == lista[meio]){
			while (valor == lista[meio-1]){
				meio = meio-1;
			}
            return meio + 1;
        }   
        if (valor < lista[meio])
            sup = meio - 1;
        else 
            inf = meio + 1;
    }


    return -1;

}

int maior(int vetor[], int tam){
	int maior = vetor[0] ;

	for (int i = 1; i < tam; i++){
		if (vetor[i] > maior)
			maior = vetor[i];

	}
	
	return maior;
}
