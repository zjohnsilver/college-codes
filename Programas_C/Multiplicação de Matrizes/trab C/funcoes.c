#include "funcoes.h"

#include <string.h>



Matriz lerMatriz(FILE *arq){

	Matriz matriz;

	int i, j;


	
//Lê quantas linhas e colunas

	fscanf(arq, "%d %d", &matriz.linha, &matriz.coluna);



	//Aloca o espaço da Matriz

	matriz.dados = malloc(sizeof(double*)*matriz.linha);


	for(i = 0; i < matriz.linha; i++){

		matriz.dados[i] = malloc(sizeof(double)*matriz.coluna);

	}


	//Ler Matriz de um arquivo

	for (i = 0; i < matriz.linha; ++i){

		for (j = 0; j < matriz.coluna; ++j){

			fscanf(arq, "%lf", &matriz.dados[i][j]);
 
		}

	}


	return matriz;

}



//Desaloca os espaços alocados

void clearDados(Matriz a){

	int i;


	for(i = 0; i < a.linha; i++){

		free(a.dados[i]);

	}

	free(a.dados);

}



//Multiplica a Matriz

void multMatriz(Matriz a, Matriz b){


	//Verifica se é possível multiplicar

	if(a.coluna == b.linha){

		int i, j, k;


		Matriz c;



		c.linha = a.linha;

		c.coluna = b.coluna;


		c.dados = malloc(sizeof(double*)*c.linha);



		for(i = 0; i < c.linha; i++){

			c.dados[i] = malloc(sizeof(double)*c.coluna);

		}



		for(i = 0; i < a.linha; i++){
			for(j =  0; j < b.coluna; j++){

				c.dados[i][j] = 0;

				for (k = 0; k < a.coluna ; k++){

					c.dados[i][j] += a.dados[i][k]*b.dados[k][j];

				}

			}

		}


		clearDados(a);

		clearDados(b);


		for (i = 0; i < c.linha; i++){

			for (j = 0; j < c.coluna; j++){

				printf("%lf ", c.dados[i][j]);

			}

			printf("\n");

		}



		criaArqSaida(c);

	}


	else{

		printf("As matrizes não podem ser multiplicadas.\n");

		exit(EXIT_FAILURE);

	}


}



//Cria o terceiro arquivo

void criaArqSaida(Matriz a){

	int i, j;


	FILE *arq = fopen("Matriz_Final.txt", "w");



	fprintf(arq, "%d\t%d\n", a.linha, a.coluna);


	
for(i = 0; i < a.linha; i++){

		for(j = 0; j< a.coluna; j++){

			fprintf(arq, "%lf\t", a.dados[i][j]);

		}

		fprintf(arq, "\n");

	}


	fclose(arq);

}