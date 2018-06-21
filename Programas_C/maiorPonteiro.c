//
// Maior numero em um vetor random, usando ponteiro. Multiplique maior por menor.
//
// Created by Jon in 22.03.2016
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAM 40
#define MAX 20
#define MIN 1

int main(){
    int i, vetor[TAM], *maior = NULL, *menor = NULL, *vet = NULL;
    vet = vetor;
    srand ((unsigned int) time(NULL));
    for (i=0; i<TAM; i++){
        *(vet + i) = MIN + rand() %MAX;
        printf ("%d\n", *(vet+i));
    }
    maior = vet;
    menor = vet;
    for (i=1; i<TAM; i++){
        if (*maior < *(vet + i)){
            maior = vet+i;
        }
        if (*menor > *(vet +i)){
            menor = vet+ i;
        }
    }
    printf ("Maior- %d, Menor - %d\n", *maior, *menor);
    printf ("Produto entre os dois: %d", (*maior)* (*menor));


    return 0;
}
