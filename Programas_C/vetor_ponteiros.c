#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10

int main(){
	int **pmatriz = NULL, colunas, linhas, i, j;
	
	//Semente da funcao rand()
	srand ((unsigned) time(NULL));

	printf ("Linhas da matriz: ");
	scanf ("%d", &linhas);

	//Alocando o vetor de ponteiros(MATRIZ), LINHAS.....
	pmatriz = (int **)  malloc(linhas*sizeof(int *));
	
	//Verificando se a memoria e insuficiente
	if (!(pmatriz)){
		exit(1);
	}

	printf ("Colunas da matriz: ");
	scanf ("%d", &colunas);
	
	//Alocando o tamanho de cada linha -- (Tamanho == Colunas)
	for (i = 0; i<linhas; i++){
		*(pmatriz + i) = (int *) malloc(colunas*sizeof(int));
		//Verificando se a memoria e insuficiente
		if (!(*(pmatriz+i))){
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

	//Liberando a memoria alocada
	for (j = 0; j<linhas; j++){
		free( *(pmatriz + j) );
	}

	return 0;
}
