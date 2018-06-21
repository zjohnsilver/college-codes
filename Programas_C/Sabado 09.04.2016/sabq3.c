#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define TAM 8
#define MAX 10

void ordena_CorD(int *px, char CordD);

int main(){
	int y, vetor[TAM], *pvetor = NULL;
	char cD;
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
	printf ("Crescente 'C', Decrescente 'D': ");
	scanf ("%c", &cD);
	printf ("\n");
	
	ordena_CorD(pvetor, cD);
	
	printf ("VETOR ORDENADO: \n");
	for (y=0; y<TAM; y++){
		printf ("%d  ", *(pvetor + y));
	
	}
	printf ("\n");

	return 0;
}

void ordena_CorD(int *px, char CordD){
	int i, l;
	
	if (CordD == 'C'){
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
	if (CordD == 'D'){
		for (i=0; i<TAM-1; i++){
			for (l=i+1; l<TAM; l++){
				if (*(px + i ) < *(px+l)){
					*(px + i) = *(px+i) ^ *(px+l);
					*(px + l) = *(px+i) ^ *(px+l);
					*(px + i) = *(px+i) ^ *(px+l);
				}
			}

		}
	}
	
}



