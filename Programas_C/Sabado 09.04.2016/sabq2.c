#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define TAM 8
#define MAX 10

void invert_Vetor(int *px);

int main(){
	int y, vetor[TAM], *pvetor = NULL;
	srand ((unsigned) time(NULL));
	pvetor = vetor;
	for (y=0; y<TAM; y++){
		*(pvetor + y) = rand() % MAX;
	
	}
	printf ("VETOR: \n");
	for (y=0; y<TAM; y++){
		printf ("%d  ", *(pvetor + y));
	
	}
	
	printf ("\n\n");
	
	invert_Vetor(pvetor);
	
	printf ("VETOR INVERTIDO: \n");
	for (y=0; y<TAM; y++){
		printf ("%d  ", *(pvetor + y));
	
	}
	printf ("\n");

	return 0;
}

void invert_Vetor(int *px){
	int i, l = TAM-1;
	for (i=0; i<TAM/2; i++){
		*(px + i) = *(px+i) ^ *(px+l);
		*(px + l) = *(px+i) ^ *(px+l);
		*(px + i) = *(px+i) ^ *(px+l);
		l-=1;	
	}
}


