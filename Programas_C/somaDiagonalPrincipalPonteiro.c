#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10
#define TAM 4

int main(int argc, char argv[]){
	int *pont = NULL, soma = 0;
	int i;

	pont = (int *) malloc(TAM*TAM*sizeof(int));

	//pont = matriz[0];
		
	srand((unsigned) time(NULL));

	// Preenchendo a matriz
	for (i = 0; i<TAM*TAM; i++){
		*(pont + i) = (rand() % MAX) + 1;
	}


	//IMPRIMINDO A MATRIZ
	for (i = 0; i<TAM*TAM; i++){
		if (!(i%TAM) && i!=0){
			printf ("\n");
		}
		printf("%i\t", *(pont + i));

	}

	for (i = 0; i<TAM*TAM; i++){
		if (!(i%(TAM+1))){
			soma += *(pont + i);
		}
	}	

	printf ("\n\nSoma da Diagonal Principal: %d\n\n", soma);

	return 0;
}