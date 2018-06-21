//
//Ordena os itens de um vetor em ordem Crescente;
//
// Created by Jon 01.03.2016
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define BEG -300
#define FIN 601
#define TAM 100

int main(){
    int vetor_[TAM], j, l, qtd_0=0, qtd_1=0;
    srand((unsigned int) time(NULL));
    printf ("VETOR PSEUDO ALEATORIO:\n");
    for (j=0; j<TAM; j++){
        vetor_[j] = BEG + (rand()%FIN);
        printf ("Numero: %d.\n", vetor_[j]);
    }
    printf ("\n");
    for (j=0; j<TAM;j++){
        l = j;
        while (l<TAM){
            if (vetor_[j]>vetor_[l]){
                vetor_[j] = vetor_[j] ^ vetor_[l];
                vetor_[l] = vetor_[j] ^ vetor_[l];
                vetor_[j] = vetor_[j] ^ vetor_[l];
            }
            l++;
        }
    }
    printf ("-----VETOR ORDENADO-----\n");
    for (j=0; j<TAM; j++){
        printf ("Numero: %d.\n", vetor_[j]);
    }


    return 0;
}
