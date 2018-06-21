#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define LINHA 3
#define COLUNA 3
#define MAX 104
#define MIN 4
#define RESET   "\033[0m"
#define BOLDRED     "\033[1m\033[31m"      /* Vermelho Negrito */

int main(){	
	int i, j, *pp[COLUNA], v1[LINHA], v2[LINHA], v3[LINHA];	
	srand ( (unsigned) time(NULL) );
	
	for (i=0; i< LINHA; i++){
		v1[i] = MIN + rand() % MAX;
	} 
	printf ("\n");

	for (i=0; i< LINHA; i++){
		v2[i] = MIN + rand() % MAX;
	} 
	printf ("\n");

	for (i=0; i< LINHA; i++){
		v3[i] = MIN + rand() % MAX;
	} 
	printf ("\n");
	pp[0] = v1;
	pp[1] = v2;
	pp[2] = v3;

	for (i = 0; i< COLUNA; i++){
		for (j=0; j< LINHA; j++){
			if (j==i){ //0 4 8
				printf (BOLDRED"%d\t", *(pp[j] + i) );
			}

			else{
				printf (RESET"%d\t", *(pp[j] + i) );
			}
		}
		printf ("\n\n" RESET);
	}
	
	return 0;
}
