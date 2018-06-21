#include <stdio.h>
#include <stdlib.h>

typedef struct matriz{
	int linha;
	int coluna;
	double **dados;
} Matriz;

Matriz lerMatriz(FILE *arq);

void criaArqSaida(Matriz x);

void clearDados(Matriz x);