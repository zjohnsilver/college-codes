#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define NL 7
#define NC 4
#define MAX 10

void povoar_matriz (int *matriz);
void mostrar_vetor (int *matriz, int linhas, int colunas);
void matriz_transposta (int *matriz, int *matriz2);


int main(){
	int mat[NL][NC], mat_transp[NC][NL];

	srand ( (unsigned) time(NULL) );
	povoar_matriz (mat[0]);

	printf ("Matriz: \n");
	mostrar_vetor (mat[0], NL, NC);
	printf ("\n\n");

	matriz_transposta (mat[0], mat_transp[0]);

	printf ("Matriz Transposta: \n");
	mostrar_vetor (mat_transp[0], NC, NL);

	printf ("\n");

	return 0;
}


void povoar_matriz (int *matriz){
	int i;

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


void mostrar_vetor (int *matriz, int linhas, int colunas){
	int i;

	for (i=0; i<linhas*colunas; i++){
		if (i%colunas == 0){
			printf ("\n");
		} 

		printf ("%d  ", *(matriz + i));
	}
}



