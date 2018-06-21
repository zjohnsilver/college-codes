#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10;

struct matrix{
	int nl;
	int nc;
	int mx;
	int *pdata;
	
};


int main(){
	int i;
	
	srand ((unsigned) time(NULL));

	struct matrix mat;

	mat.mx = MAX;
	
	printf ("Linhas: ");
	scanf ("%d", &mat.nl);
	printf ("Colunas: ");
	scanf ("%d", &mat.nc);

	mat.pdata = (int *) malloc (mat.nl * mat.nc *sizeof (int));

	for (i=0; i<mat.nl*mat.nc; i++){
		*(mat.pdata + i) = i;

	}
	for (i=0; i<mat.nl*mat.nc; i++){
		if (!(i%mat.nc)){
			printf ("\n");
		}
		printf ("%d  ", *(mat.pdata + i));

	}

	printf ("\n\n");
	return 0;
}
