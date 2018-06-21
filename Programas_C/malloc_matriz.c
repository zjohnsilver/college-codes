
// Feito em 19/04/2016 by Jhon

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10
void somatorio (int *pvetor, int tam, int *soma);
void mostrar_matriz(int *px, int linha, int coluna);
void preencher_matriz(int *px, int linha, int coluna);
void produtorio (int *pvetor, int tam, int *produtorio);
void exeOp(void (*funcao)(), int *pmatriz, int linha, int coluna, int *result);

int main(int argc, char *argv[]){
	if (argc == 3){
		int *matriz = NULL, x, ordem_matriz, resultado;
		void (*funcao)(); //Ponteiro para funcao.
	
		x = atoi(argv[1]); //Variavel que sera testada: PAR/IMPAR. 
		ordem_matriz = atoi(argv[2]);

		funcao = (x%2)?produtorio:somatorio; //Ternario: Produtorio se for impar, Somatorio se for par.

		matriz = (int *) malloc(ordem_matriz*ordem_matriz*sizeof(int)); //Funcao malloc, alocacao dinamica de matriz.
	
		preencher_matriz(matriz, ordem_matriz, ordem_matriz);
		mostrar_matriz(matriz, ordem_matriz, ordem_matriz);
		
		exeOp (funcao, matriz, ordem_matriz, ordem_matriz, &resultado);

		// Ternario para imprimir o Produtorio ou o Somatorio.
		(x%2)?printf ("\n\nProdutorio da diagonal Principal: %d\n", resultado):printf ("\n\nSomatorio da Diagonal Principal: %d\n", resultado);

	}	
	else{
		printf ("\nVoce nao forneceu a quantidade necessaria de argumentos.\n\n");
		printf ("Entradas feitas pelo terminal...\n\n");
		exit(1);
	}

	return 0;
}


void mostrar_matriz(int *px, int linha, int coluna){
	int i;
	
	for (i = 0; i < linha*coluna; i++){
		if (!(i%coluna)){
			printf ("\n");
		}
		printf ("%d   ", *(px + i));
	}
}


void preencher_matriz(int *px, int linha, int coluna){
	int i;
	srand ((unsigned) time(NULL));

	for (i = 0; i < linha*coluna; i++){
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


void exeOp(void (*funcao)(), int *pmatriz, int linha, int coluna, int *result){
	int i, x=0, *diag_principal = NULL;

	diag_principal = (int *) malloc(linha * sizeof(int));	
	
	//Preenchendo vetor com os elementos da diagonal principal.
	for (i = 0; i<linha*coluna; i++){
		if (i%(coluna+1) == 0){
			*(diag_principal + x) = *(pmatriz +i);
			x++;
		}
	}

	//Executando a funcao correspondente.

	(*funcao)(diag_principal, linha, result);
}

