////////////////////////////////////////////
// Problema 1013 URI: O Maior			  //
//                                        //
// Feito por Lancelot                     //
//                                        //
// Data: 11/12/16                         //
////////////////////////////////////////////


#include <stdio.h>
 
int main() {
 
    int A, B, C, Maior, Maior2;

	scanf ("%i%i%i", &A, &B, &C);
	Maior = (A+B + abs(A-B))/2;
	Maior2 = (Maior+C+ abs(Maior-C))/2;
	
	printf ("%i eh o maior\n", Maior2);
 
    return 0;
}