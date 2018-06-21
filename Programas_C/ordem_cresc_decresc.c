#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10

void ordem (int *vetor, char *ordem, int *tamanho);
void preencher_vetor (int *vetor, int *tamanho);
void mostrar_vetor (int*vetor, int *tamanho);

int main(int argc, char *argv[]){ //ou **argv
	int tamanho, *vetor = NULL;
	char tipo;
	tamanho = atoi(argv[1]); //Entrada feita pelo terminal
	
	printf ("C-Crescente ou D-Decrescente: ");
	scanf ("%c", &tipo);

	//Alocando vetor dinamicamente malloc();
	vetor = (int *) malloc (tamanho*sizeof(int));

	//Preenchendo o vetor
	preencher_vetor (vetor, &tamanho);

	//Mostrando o vetor
	printf ("VETOR:\n\t");
	mostrar_vetor (vetor, &tamanho);

	//Ordenando o vetor
	ordem (vetor, &tipo, &tamanho);
	
	printf ("\n\n");
	//Mostrando o vetor
	printf ("VETOR ORDENADO:\n\t");
	mostrar_vetor (vetor, &tamanho);

	printf ("\n\n");

	return 0;
}

void preencher_vetor (int *vetor, int *tamanho){
	int i;

	//Semente da funcao rand();
	srand ((unsigned) time(NULL));

	//Preenchendo o vetor;
	for (i=0; i<*tamanho; i++){
		*(vetor + i) = rand() % MAX;
	}

}

void mostrar_vetor (int*vetor, int *tamanho){
	int i;

	//Mostrando o vetor;
	for (i=0; i<*tamanho; i++){
		printf ("%d\t", *(vetor + i));
	}


}


void ordem (int *vetor, char *ordem, int *tamanho){
	int i, j;
	// Metodo geral de ordenacao BOLHA

	// Ordenada Crescentemente
	if (*ordem == 'C'){
		for (i=0; i<*tamanho-1; i++){
			for (j=i+1; j<*tamanho; j++){
				if (*(vetor+i)>*(vetor+j)){
					*(vetor+i) = *(vetor+i) ^ *(vetor+j);
					*(vetor+j) = *(vetor+i) ^ *(vetor+j);
					*(vetor+i) = *(vetor+i) ^ *(vetor+j);
				}
			}
		}
	}
	//Ordena Decrescentemente 
	if (*ordem == 'D'){
		for (i=0; i<*tamanho-1; i++){
			for (j=i+1; j<*tamanho; j++){
				if (*(vetor+i)<*(vetor+j)){
					*(vetor+i) = *(vetor+i) ^ *(vetor+j);
					*(vetor+j) = *(vetor+i) ^ *(vetor+j);
					*(vetor+i) = *(vetor+i) ^ *(vetor+j);
				}
			}
		}
	}
} 
