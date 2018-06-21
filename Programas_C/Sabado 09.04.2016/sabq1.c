#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define TAM 5
#define MAX 10

void invert_X(int *px, int x);

int main(){
	int y, vetor[TAM], X, *pvetor = NULL;
	srand ((unsigned) time(NULL));
	pvetor = vetor;
	for (y=0; y<TAM; y++){
		*(pvetor + y) = rand() % MAX;
	
	}
	printf ("VETOR: \n");
	for (y=0; y<TAM; y++){
		printf ("%d  ", *(pvetor + y));
	
	}
	printf ("\n");
	printf ("Valor de X: ");
	scanf ("%d", &X);
	
	invert_X(pvetor, X);
	
	printf ("VETOR com valores %d INVERTIDOS: \n", X);
	for (y=0; y<TAM; y++){
		printf ("%d  ", *(pvetor + y));
	
	}
	printf ("\n");

	return 0;
}

void invert_X(int *px, int x){
	int i;
	for (i=0; i<TAM; i++){
		if (*(px + i) == x){
			*(px+i) *= (-1);
		}	
	}
}
