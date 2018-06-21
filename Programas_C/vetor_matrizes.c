#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10;
#define TOTAL 1000

struct matrix{
	unsigned short int nl, nc, mx;
	unsigned char *pdata;
	
};


int main(){
	int i, j;
	
	srand ((unsigned) time(NULL));

	struct matrix mat[TOTAL];

	for (i=0; i<TOTAL; i++){
		mat[i].nl = 3 + rand() % 8;
		mat[i].nc = 3 + rand() % 8;
		mat[i].mx = 10 + rand()% 11;
		mat[i].pdata = (unsigned char *) malloc (mat[i].nl * mat[i].nc *sizeof (int));

		if (!(mat[i].pdata)){
			puts ("MEMORIA INSUFICIENTE");
			exit(1);
		}

		for (j=0; j<mat[i].nl*mat[i].nc; j++){
			*(mat[i].pdata + j) = rand() % mat[i].mx; 
		}
		
		printf ("MATRIZ %d:\n", i+1);
		for (j=0; j<mat[i].nl*mat[i].nc; j++){
			if (!(j%mat[i].nc)){
				printf ("\n");
			}
			printf ("%d\t", *(mat[i].pdata + j));
		}
		printf ("\n\n");
	}


	return 0;
}
