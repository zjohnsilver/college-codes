//
// Quadrado dos multiplos de 4, na faixa fornecida pelo usuario.
//
// Created by Jon in 02.03.2016
//
#include <stdio.h>

int main(){
    int ini, fim , j;;

    printf ("Inicio da faixa: ");
    scanf ("%d", &ini);

    printf ("Fim da faixa: ");
    scanf ("%d", &fim);
    if (ini>fim){
        ini = ini^fim;
        fim = ini^fim;
        ini = ini^fim;
    }

    for (j=ini; j<=fim;j++){
        if (!(j%4)){
            printf ("\nQuadrado de %i : %i\n", j, j*j);
        }
    }

    system ("PAUSE");
    return 0;
}
