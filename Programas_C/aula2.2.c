//
// Minha Declaração a Andressa
//
// Created by Jon in 02.03.2016
//

#include <stdio.h>

int main(){
    int opcao;
    char answer;
    printf ("Ola Andressa, escolha uma das perguntas abaixo, digitando o respectivo numero.\n");
    printf ("Por enquanto tem apenas uma pergunta kkk");
    printf ("1 - Joao Carlos lhe ama? \n");


    do{
        printf ("Para encerrar o programa, e ver uma mensagem final, digite 0 <-(Zero)\n");
        printf ("Opcao: ");
        scanf ("%d", &opcao);
        getchar();
        if (opcao==1){
           printf ("Responda S para Sim e N para nao: \n");
           scanf ("%c", &answer);
           if (answer == 'S'){
                printf ("Ama mesmo =D\n");

           }
           else if (answer == 'N'){
                printf ("        ***         ***   \n");
                printf ("      *     *     *     * \n");
                printf ("      *   I   *  * LOVE  * \n");
                printf ("       *       *        * \n");
                printf ("         *  ANDRESSA  * \n");
                printf ("          *          * \n");
                printf ("            *  YOU * \n");
                printf ("              *   * \n");
                printf ("                *\n");
           }
        }

    }while (opcao>0);
    printf ("\nVoce ja me salvou muitas vezes, e nem tem nocao disso.\n");
    printf ("Obrigado Andressa, Eu te amo <3\n\n");


    system ("PAUSE");
    return 0;
}
