#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NL 7
#define NC 4
#define MAX 10

void povoar_matriz (int *matriz);
void mostrar_matriz (int *matriz, int linhas, int colunas);
void matriz_transposta (int *matriz, int *matriz2);


int main(){
	int mat[NL][NC], mat_transp[NC][NL];

	//Funcao que povoa a matriz
	povoar_matriz (mat[0]);

	//Funcao que mostra a matriz
	mostrar_matriz (mat[0], NL, NC);

	printf ("\n\n");

	//Calculando a matriz transposta
	matriz_transposta (mat[0], mat_transp[0]);

	//Mostrando matriz transposta
	mostrar_matriz (mat_transp[0], NC, NL);

	printf ("\n");

	return 0;
}


void povoar_matriz (int *matriz){
	int i;
	
	//Semente da funcao rand();
	srand ( (unsigned) time(NULL) );

	for (i=0; i<NL*NC; i++){
		*(matriz+i) = rand() % MAX;
	}
}


void matriz_transposta (int *matriz, int *matriz2){
	int i, x = 0, y = 1; 

	for (i = 0; i < NL*NC; i++){
		if (i%NC==0 && i!=0){
			x = y;
			y+=1;
		}
		*(matriz2 + x) = *(matriz + i);
		x += NL;
	}
}


void mostrar_matriz (int *matriz, int linhas, int colunas){
	int i;

	for (i=0; i<linhas*colunas; i++){
		if (i%colunas == 0){
			printf ("\n");
		} 
		printf ("%d  ", *(matriz + i));
	}
}



