//
// Fatorial dos números ímpares na faixa [1,10]
//
// Created by Jon in 03.03.2016
//
#include <stdio.h>


int main(){
    int i, j, fat;
    printf ("\n----- FATORIAIS -----\n\n");
    for (j=1; j<10; j+=2){
        fat=1;
        for (i=j; i>=1;i--){
            fat = fat*i;
        }
        printf ("FATORIAL DE %i: %i\n", j, fat);
    }

    system ("PAUSE");
    return 0;
}
