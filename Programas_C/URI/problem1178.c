// Problema 1178 URI: Preenchimento de Vetor III //
//                                        		 //
// Feito por Lancelot                     		 //
//                                        		 //
// Data: 16/12/16                         		 //
///////////////////////////////////////////////////

#include <stdio.h>
#define TAM 100

int main() {
	int i;
	double N[TAM];  //Declarando variáveis
 
	scanf ("%lf", &N[0]); //Recebendo o valor que vai ser a base do vetor (posicao 0)

	//Laco para percorrer o vetor e imprimi-lo
	for (i = 0; i < TAM; i++){
		printf ("N[%i] = %.4lf\n", i, N[i]);
		N[i + 1] = N[i] / 2; 
	}

	return 0;
}
