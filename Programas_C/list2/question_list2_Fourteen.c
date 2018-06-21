//
// Quantidade de divisores por 3 entre [A,B]
//
// Created by Jon in 03.03.2016
//

#include <stdio.h>

int main(){
    int i, ini, fim, cont=0;
    printf ("\n-----PROGRAMA QUE DIZ A QUANTIDADE DE DIVISORES POR 3 EM UM INTERVALO-----\n\n");

    printf ("Inicio: ");
    scanf ("%d", &ini);

    printf ("Fim: ");
    scanf ("%d", &fim);

    if (fim>ini){
        ini = ini^fim;
        fim = ini^fim;
        ini = ini^fim;
    }

    for (i=ini; i<=fim; i++){
        if (i%3==0){
            cont++;
        }
    }
    printf ("Quantidade de divisores por 3 entre %d e %d e %d.\n", ini, fim, cont);

    system ("PAUSE");
    return 0;
}
