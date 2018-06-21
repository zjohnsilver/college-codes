
//
// Tabuada de um valor digitado pelo usuario
//
// Created by Jon in 03.03.2016
//

#include <stdio.h>
int main(){

    int valor, i, j, opcao, ini, fim;
    printf ("-----TABUADA-----\n");

    do {
        printf ("\n\n1- Tabuada de 1 a 10.\n");
        printf ("2- Tabuada de uma faixa de valores.\n");
        printf ("3- Tabuada de um valor especifico.\n");
        printf ("4- Sair.\n");

        printf ("Opcao: ");
        scanf ("%d", &opcao);

        switch (opcao){
        case 1:
            for (i=1; i<=10;i++){
                printf ("\nTabuada do %d: \n\n", i);
                for (j=1; j<=10; j++){
                    printf ("%d x %d = %d\n", i, j, i*j);
                }
            }
            break;

        case 2:
            printf ("\nInicio: ");
            scanf ("%d", &ini);

            printf ("Final: ");
            scanf ("%d", &fim);

            for (i=ini; i<=fim;i++){
                printf ("\nTabuada do %d: \n\n", i);
                for (j=1; j<=10; j++){
                    printf ("%d x %d = %d\n", i, j, i*j);
                }
            }
            break;

        case 3:
            printf ("\nValor: ");
            scanf ("%d", &valor);

            printf ("\nTabuada do %d\n\n", valor);
            for (i=1; i<=10; i++){
                printf ("%d x %d = %d\n", valor, i, valor*i);
            }
            break;

        case 4:
            printf ("\nPrograma encerrado...\n");
            break;

        default:
            printf ("Opcao Invalida");    }

    }while (opcao!=4);


    system("PAUSE");
    return 0;
}
