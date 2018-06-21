#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10
#define LIN 8
#define COL 8

void make_Matrix(int *px);
void show_Matrix(int *px);
void rotate_Matrix(int *normal, int *recebe_Invertida);

int main(){
	int *pj = NULL, *pi = NULL, matriz1[LIN][COL], matriz2[COL][LIN];

	pj = matriz1[0];
	pi = matriz2[0];
	
	make_Matrix(pj);
	printf ("\n\n");
	printf ("MATRIZ NORMAL:\n\n");

	show_Matrix(pj);
		
	printf ("\n\n");

	rotate_Matrix(pj, pi);

	printf ("\n");

	printf ("MATRIZ INVERTIDA: \n\n");

	show_Matrix(pi);

	return 0;
}

void rotate_Matrix(int *normal, int *recebe_Invertida){
	int k = 0, x = 0, y = 0, j, i = LIN-1;
	for (j=0; j<(LIN*COL); j++){
		if (k==COL){
			i-=LIN;	
			i-= ((COL*LIN) - (LIN-1));
			k=0;
		}   
		*(recebe_Invertida+i) = *(normal+j);           	
		
		i+=LIN;
		k+=1;

	}
}

void show_Matrix(int *px){
	int j;
	for (j=0; j< LIN*COL; j++){
		printf ("%i   ", *(px + j));
		if ((j+1) % COL == 0){
	   		printf ("\n\n");
		}
    }

}
void make_Matrix(int *px){
	int i;
	srand( (unsigned) time(NULL) );
	for (i=0; i<LIN*COL; i++){
		*(px+i) = rand()% MAX;
	}
}
