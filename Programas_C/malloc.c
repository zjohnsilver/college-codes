
// Feito em 19/04/2016 by Jhon

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10

void preencher_vetor(int *px, int tam);
void somatorio (int *pvetor, int tam, int *soma);
void produtorio (int *pvetor, int tam, int *produtorio);
void mostrar_vetor(int *px, int tam);

int main(int argc, char *argv[]){
	if (argc == 3){
		int *vetor = NULL, x, tam_vetor, resultado;
		void (*funcao)(); //Ponteiro para funcao.
	
		x = atoi(argv[1]); //Variavel que sera testada: PAR/IMPAR. 
		tam_vetor = atoi(argv[2]);

		funcao = (x%2)?produtorio:somatorio; //Ternario: Produtorio se for impar, Somatorio se for par.

		vetor = (int *) malloc(tam_vetor*sizeof(int)); //Funcao malloc, alocacao dinamica de vetor.
	
		preencher_vetor(vetor, tam_vetor);
		mostrar_vetor(vetor, tam_vetor);
		
		funcao(vetor, tam_vetor, &resultado);
		
		// Ternario para imprimir o Produtorio ou o Somatorio.
		(x%2)?printf ("\nProdutorio: %d\n", resultado):printf ("\nSomatorio: %d\n", resultado);

	}	
	else{
		printf ("\nVoce nao forneceu a quantidade necessaria de argumentos.\n\n");
		printf ("Entradas feitas pelo terminal...\n\n");
		exit(1);
	}

	return 0;
}


void mostrar_vetor(int *px, int tam){
	int i;
	
	for (i = 0; i < tam; i++){
		printf ("%d  ", *(px + i));
	}
}


void preencher_vetor(int *px, int tam){
	int i;
	srand ((unsigned) time(NULL));

	for (i = 0; i < tam; i++){
		*(px+i) = rand() % MAX;
	}
		
}


void somatorio (int *pvetor, int tam, int *soma){
	int i;
	*soma = 0;

	for (i = 0; i<tam; i++){
		*soma += *(pvetor + i);
	}

}


void produtorio (int *pvetor, int tam, int *produtorio){
	int i;
	*produtorio = 1;

	for (i = 0; i<tam; i++){
		*produtorio *= *(pvetor + i);
	}

}

