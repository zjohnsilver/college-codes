////////////////////////////////////////////
// Problema 1010 URI: Calculo Simples 	  //
//                                        //
// Feito por Lancelot                     //
//                                        //
// Data: 11/12/16                         //
////////////////////////////////////////////


#include <stdio.h>
 
int main() {
 
    int A, B, L, C;
	float E, D;

	scanf ("%i%i%f", &A, &B, &E);
	scanf ("%i%i%f", &L, &C, &D);
	
	printf("VALOR A PAGAR: R$ %.2f\n", B*E + C*D);
 
    return 0;
}