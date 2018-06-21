//
// Entrada e Duas prestacoes
//
// Created by Jon in 02.03.2016
//

#include <stdio.h>

int main(){
    float money=0;
    unsigned short int parc1=0, parc2=0;
    printf ("RECEBE UM VALOR E MOSTRA A DIVISAO DESSE VALOR EM 1 ENTRADA E 2 PARCELAS.\n");
    while (money<30){
        printf ("Valor: ");
        scanf ("%f", &money);
    }

    while ((money-parc1)>10&&money>parc1){
        parc1+=10;
        parc2+=10;
        money=money-20;
    }
    printf ("\nEntrada: R$%.2f; Parcelas: R$ %i.00\n", money, parc1);


    system("PAUSE");
    return 0;
}
