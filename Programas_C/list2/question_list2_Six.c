//
//Urna ELetronica
//
// Created by Jon in 01.03.2016
//
#include <stdio.h>

int main(){
    unsigned int paulo=0, renata=0, branco=0, nulo=0, qtd_Votos=0;
    int voto, test=1;
    char confirmacao = 'N';
    printf ("\n\n-----------URNA ELETRNICA----------\n\n\n");
    do{
        while (test){
            if (confirmacao=='S'){
                if (voto>=0){
                    printf ("\n-----Confirmado-----\n");
                }
                else{
                    printf ("\n\n-----PROGRAMA ENCERRADO-----\n\n");
                }
                test = 0;
            }
            else if (confirmacao == 'N'){
                printf ("\nOpcoes de voto:\n");
                puts ("5- PAULO;");
                puts ("7- RENATA;");
                puts ("0- BRANCO;");

                printf ("PARA SAIR DA VOTACAO DIGITE UM NUMERO NEGATIVO.\n");

                printf ("\nVoto: ");
                scanf ("%d", &voto);
                getchar();

                printf ("Tem certeza? S - Sim, N - Nao\n");
                scanf("%c", &confirmacao);

            }

        }
        switch(voto){
            case 5:
                paulo+=1;
                break;

            case 7:
                renata+=1;
                break;

            case 0:
                branco+=1;
                break;

            default:
                nulo+=1;
                break;
        }
        qtd_Votos+=1;
        test=1;
        confirmacao = 'N';
    }while (voto>=0);

    qtd_Votos-=1;
    nulo-=1;

    printf ("\nRESULTADO DAS VOTACOES:\n");
    if (qtd_Votos==0){
        printf ("%.2f %% - Paulo\n", 0);
        printf ("%.2f %% - Renata\n", 0);
        printf ("%.2f %% - Branco\n", 0);
        printf ("%.2f %% - Nulos\n", 0);

    }
    else{
        printf ("%.2f %% - Paulo\n", (paulo/(float)qtd_Votos)*100.0);
        printf ("%.2f %% - Renata\n", (renata/(float)qtd_Votos)*100.0);
        printf ("%.2f %% - Branco\n", (branco/(float)qtd_Votos)*100.0);
        printf ("%.2f %% - Nulos\n", (nulo/(float)qtd_Votos)*100.0);
    }

    system("PAUSE");
    system("cls");
    return 0;
}
