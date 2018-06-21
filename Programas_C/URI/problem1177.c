///////////////////////////////////////////////////
// Problema 1177 URI: Preenchimento de Vetor II  //
//                                        		 //
// Feito por Lancelot                     		 //
//                                        		 //
// Data: 16/12/16                         		 //
///////////////////////////////////////////////////


#include <stdio.h>
#define TAM 1000

int main(){
	int i, T, vetor[TAM], x = 0;

	scanf ("%i", &T);

	for (i = 0; i < TAM; i++) {
		if (x == T){
			x = 0;
		}
		vetor[i] = x;
		x++;
	}	


	for (i = 0; i < TAM; i++) {
		printf ("N[%i] = %i\n", i, vetor[i]);
	}

	return 0;
}
