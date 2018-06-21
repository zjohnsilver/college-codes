#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10
#define LIN 8
#define COL 8

void make_Matriz(int *px);

int main(){
	int k = 0, x = 0, y = 0, j, i = LIN-1, *pj = NULL, *pi = NULL, matriz1[LIN][COL];
	int matriz2[COL][LIN];

	srand ( (unsigned) time(NULL));
	pj = matriz1[0];
	pi = matriz2[0];
	
	make_Matriz(pj);
	printf ("\n\n");
	printf ("MATRIZ NORMAL:\n\n");
		
	for (j=0; j< LIN*COL; j++){
		printf ("%i   ", *(pj + j));
		if ((j+1) % COL == 0){
	   		printf ("\n\n");
		}
    }
	printf ("\n\n");
	
	for (j=0; j<(LIN*COL); j++){
		if (k==COL){
			i-=LIN;	
			i-= ((COL*LIN) - (LIN-1));
			k=0;
		}   
		*(pi+i) = *(pj+j);           	
		
		i+=LIN;
		k+=1;

	}
	printf ("\n");

	printf ("MATRIZ INVERTIDA: \n\n");

	for (j=0; j< LIN*COL; j++){
		printf ("%i   ", *(pi + j));
		if ((j+1) % LIN == 0){
	   		printf ("\n\n");
		}
    }
	return 0;
}

void make_Matriz(int *px){
	int i;
	srand( (unsigned) time(NULL) );
	for (i=0; i<LIN*COL; i++){
		*(px+i) = rand()% MAX;
	}
}
