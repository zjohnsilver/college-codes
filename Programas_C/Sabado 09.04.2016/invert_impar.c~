#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 101

void invert_impar (int *vetor, int tam);

int main(){
	int *vetor = NULL, tamanho, i, j, x;

	//Semente da funcao rand();
	srand ((unsigned) time(NULL));

	printf ("TAMANHO DO VETOR: ");	
	scanf ("%d", &tamanho);

	//Alocando dinamicamente
	vetor = (int *) malloc (tamanho*sizeof(int));
		
	//Povoando vetor
	for (i=0; i<tamanho; i++){
		*(vetor + i) = rand() % MAX;
	}

	//Mostrando vetor
	printf ("VETOR:\n\t");
	for (i=0; i<tamanho; i++){
		printf ("%d\t", *(vetor +i));
	}
	
	printf ("\n\n");

	//Usando funcao que invert os index impares de um vetor
	invert_impar (vetor, tamanho);	

	//Mostrando vetor com elementos das posições impares invertidos
	printf ("VETOR INVERTIDO NOS INDEX IMPARES:\n\t");
	for (i=0; i<tamanho; i++){
		printf ("%d\t", *(vetor +i));
	}
	
	printf ("\n\n");
	
	free(vetor);

	return 0;
}

void invert_impar (int *vetor, int tam){
	int i, j = tam-1, x; //j recebe o primeiro valor 

	for (i=0; i<tam/2; i++){ //Laco so vai ate a metade do vetor, pois, se nao, desinverteria	
		if (j%2){ 
			x = j; //Salvando o index impar ao contrario
		}
		if (i%2){ //invertendo valores
			*(vetor + i) = *(vetor + i) ^ *(vetor + x);
			*(vetor + x) = *(vetor + i) ^ *(vetor + x);
			*(vetor + i) = *(vetor + i) ^ *(vetor + x);
		}	
		j--; //Decrementando variavel que esta percorrendo o vetor de tras para frente
	}
}


