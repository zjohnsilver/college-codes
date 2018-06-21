#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10


void moda(int **matriz, int *pmoda, int ordem);

int main(){
	int **pmatriz = NULL, *moda = NULL, colunas, linhas, i, j, soma = 0, ordem;
	
	//Semente da funcao rand()
	srand ((unsigned) time(NULL));

	printf ("Linhas da matriz: ");
	scanf ("%d", &linhas);

	//Alocando o vetor de ponteiros(MATRIZ), LINHAS.....
	pmatriz = (int **)  malloc(linhas*sizeof(int *));
	
	//Verificando se a memoria e insuficiente
	if (pmatriz == NULL){
		exit(1);
	}

	printf ("Colunas da matriz: ");
	scanf ("%d", &colunas);
	
	//Alocando o tamanho de cada linha -- (Tamanho == Colunas)
	for (i = 0; i<linhas; i++){
		*(pmatriz + i) = (int *) malloc(colunas*sizeof(int));

		//Verificando se a memoria e insuficiente
		if (*(pmatriz+i) == NULL){
			exit(1);
		}
	}
	
	//Preenchendo e imprimindo a MATRIZ
	for (i=0; i<linhas; i++){
		for (j = 0; j<colunas; j++){
			*(*(pmatriz + i)+j) = rand() % MAX;
			printf ("%d\t", *(*(pmatriz + i)+j));
		}
		printf ("\n");
	}	
	//So funciona se linhas == colunas
	ordem = linhas; // Linhas == COlunas, entao ordem pode receber qualquer um dos dois.

	//for que percorre a matriz e soma a diagonal secundaria
	for (i=0; i<linhas; i++){
		for (j = 0; j<colunas; j++){
			if (i+j==(ordem-1)){
				soma += *(*(pmatriz + i)+j);
			}
		}
		printf ("\n");
	}

	printf ("SOMA DA DIAGONAL SECUNDARIA: %d\n", soma);

	//Liberando a memoria alocada
	for (j = 0; j<linhas; j++){
		free( *(pmatriz + j) );
	}

	return 0;
}


void moda(int **px, int *m1, int *pk){ // (pvetor, moda1, pka);
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
