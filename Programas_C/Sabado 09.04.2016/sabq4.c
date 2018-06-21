#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#define TAM 6
#define MAX 3

void bolha_Cresc(int *px);
float media_Aritmetica(int *px);
double media_Geometrica(int *px);
double desvio_Padrao(int *py);
float mediana(int *px);
void moda(int *px, int *m1, int *pka);

int main(){
    int y, vetor[TAM], modas[TAM], *pvetor = NULL, *moda1 = NULL, *pka = NULL, k=-1;
    char opcao;
    srand ((unsigned) time(NULL));
    pvetor = vetor;
    moda1 = modas;
    pka = &k;

    for (y=0; y<TAM; y++){
        *(pvetor + y) = 1+rand() % MAX;

    }
    printf ("VETOR: [  ");
    for (y=0; y<TAM; y++){
        printf ("%d  ", *(pvetor + y));

    }
    bolha_Cresc(pvetor);
    printf ("]");
    printf ("\n A- M.Aritmetica\n G- M-Geometrica\n D- Desvio\n E- Mediana\n O- Moda\n");
    printf ("Opcao: ");
    scanf ("%c", &opcao);
    printf ("\n");
    switch (opcao){
        case 'A':
            printf ("Media Artitmetica: %.2f", media_Aritmetica(pvetor));
            break;
        case 'G':
            printf ("Media Geometrica: %.2lf", media_Geometrica(pvetor));
            break;
        case 'D':
            printf ("Desvio Padrão: %.2lf", desvio_Padrao(pvetor));
            break;
        case 'E':
            printf ("Mediana: %.2f", mediana(pvetor));
            break;
        case 'O':
            moda(pvetor, moda1, pka);

            printf ("Modas: ");
            if (*pka != -1){
                mostrar_Vetor(moda1, *pka+1);
                printf ("\n\n%d Modas.\n", *pka+1);
            }
            else{
                printf ("Nao ha Moda.");
            }
            break;

    }
    printf ("\n\n");

    return 0;
}

float media_Aritmetica(int *px){
    int i, soma=0;
    float media;
    for (i=0; i<TAM; i++){
        soma += *(px+i);

    }
    media = ((float)soma)/TAM;
    return media;
}

double media_Geometrica(int *px){
    int i, produto=1;
    double media;
    for (i=0; i<TAM; i++){
        produto *= *(px+i);

    }
    media = pow(produto, (1.0/TAM));

    return media;
}

double desvio_Padrao(int *py){
    int i, soma = 0;
    double desvioP;
    for (i=0; i<TAM; i++){
        soma += pow(*(py+i) - media_Aritmetica(py), 2);

    }
    desvioP = pow((1.0/(TAM-1))*soma, (1.0/2));

    return desvioP;
}



float mediana(int *px){
    int i;
    float median;
    if (TAM % 2 == 0){
        for (i=0; i<TAM; i++){
            median = (*(px + TAM/2) + *(px + (TAM-1)/2))/2.0;
        }
    }
    else{
        median = *(px + (TAM-1)/2);
    }
    return median;
}


void moda(int *px, int *m1, int *pk){ // (pvetor, moda1, pka);
    int i, l, qtd, geral=0, test = 0;

    for (i=0; i<TAM-1; i++){
        qtd = 0;
        for (l=i+1; l<TAM; l++){
            if (*(px + i) == *(px + l)){
                qtd+=1;
            }
        }
        if (qtd > geral){
            *pk=0;
            geral = qtd;
            *(m1 + *pk) = *(px + i);
            test = 1;
        }
        else if ((qtd == geral) & test){
            *pk+=1;
            *(m1 + (*pk)) = *(px + i);

        }
    }
}

void bolha_Cresc(int *px){
    int i, l;

    for (i=0; i<TAM-1; i++){
        for (l=i+1; l<TAM; l++){
            if (*(px + i) > *(px + l)){
                *(px + i) = *(px+i) ^ *(px+l);
                *(px + l) = *(px+i) ^ *(px+l);
                *(px + i) = *(px+i) ^ *(px+l);
            }
        }
    }
}

void mostrar_Vetor(int *px, int tam){
    int i;
    for (i=0; i<tam; i++){
        printf ("%d  ", *(px+i));
    }
}
