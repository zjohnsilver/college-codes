#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 20

void preencher_vetor(int *px, int tam);

int main(){
	int tamanho, *vetor, i, novo_tamanho;
	
	printf("Tamanho: ");
	scanf ("%d", &tamanho);
 	
	// Alocação dinâmica para dados no vetor
    //vetor = (int*) malloc(tamanho * sizeof(int));
	vetor = (int *) malloc(tamanho * sizeof(int));

	if (!vetor){ // if (vetor == NULL)
		puts ("Sem Memória!!!\n");
		exit(1);
	}

	preencher_vetor (vetor, tamanho);

	// Mostrando vetor
	for (i = 0; i< tamanho; i++){
		printf ("[%d]\t[%p]\t[%d]\n", i, vetor + i, *(vetor+i));
	}
	printf ("\n\n---------------\n\n");

	printf("Novo Tamanho: ");
	scanf ("%d", &novo_tamanho);

	// Realocar memoria
	vetor = (int *) realloc(vetor, novo_tamanho * sizeof(int));
	
	//Mostrando vetor
	for (i = 0; i< novo_tamanho; i++){
		printf ("[%d]\t[%p]\t[%d]\n", i, vetor + i, *(vetor+i));
	}

	free (vetor); // Desalocar memoria
	return 0;
}

 
void preencher_vetor(int *px, int tam){
    int i;

	//Configurando semente do rand()
    srand ((unsigned) time(NULL));
 
    for (i = 0; i < tam; i++){
        *(px+i) = rand() % MAX;
    }
         
}










