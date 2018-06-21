#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NL 4
#define NC 5
#define MAX 10

void povoar_matriz (int *matriz);
void mostrar_vetor (int *matriz, int linhas, int colunas);
void matrans (int *matriz, int *matriz2);

int main(){
	int mat[NL][NC], matrans[NC][NL];

	srand ( (unsigned) time(NULL) );
	povoar_matriz (mat[0]);

	mostrar_vetor (mat[0], NL, NC);
	printf ("\n\n");

	matrans (mat[0], matrans[0]);

	mostrar_vetor (matrans[0], NC, NL);
}


void povoar_matriz (int *matriz){
	int i;

	for (i=0; i<NL*NC; i++){
		*(matriz+i) = rand() % MAX;
	}
}

void matrans (int *matriz, int *matriz2){
	int i, x=0;
	
	for (i = 0; i<NL*NC; i++){
		*(matriz2 + i + x) = *(matriz +i);
		x++; 	
	}

}

void mostrar_vetor (int *matriz, int linhas, int colunas){
	int i;

	for (i=0; i<linhas*colunas; i++){
		if (i%colunas == 0){
			printf ("\n");
		} 

		printf ("%d  ", *(matriz + i));
	}

}



