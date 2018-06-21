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

	return 0;
}

void invert_impar (int *vetor, int tam){
	int i, j; //j recebe o primeiro valor

	j = ((tam-1)%2)?(tam-1):(tam-2);

	for (i=1; i<tam/2; i+=2){ //Laco so vai ate a metade do vetor, pois, se nao, desinverteria	
		*(vetor + i) = *(vetor + i) ^ *(vetor + j);
		*(vetor + j) = *(vetor + i) ^ *(vetor + j);
		*(vetor + i) = *(vetor + i) ^ *(vetor + j);	
		j-=2; //Decrementando variavel que esta percorrendo o vetor de tras para frente
	}
}


