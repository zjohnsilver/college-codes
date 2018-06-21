#include <stdio.h>
#define TAM 20

int main(){
    int x, y;
    int vetor[5];

    srand ((unsigned) time(NULL));

    for (x=0; x<5; x++){
        vetor[x] = rand() % TAM + 1;
    }
    for (x=0; x<4; x++){
        for (y = x; y < 5; y++){
            if (vetor[x] > vetor[y]){
                vetor[x] = vetor[x] ^ vetor[y];
                vetor[y] = vetor[x] ^ vetor[y];
                vetor[x] = vetor[x] ^ vetor[y];
            }
        }
    }
    for (x=0; x<5; x++){
        printf ("Valor: %i\n", vetor[x]);
    }

    return 0
}


