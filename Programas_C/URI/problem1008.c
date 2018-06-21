////////////////////////////////////////////
// Problema 1008 URI: Salario	  		  //
//                                        //
// Feito por Lancelot                     //
//                                        //
// Data: 11/12/16                         //
////////////////////////////////////////////


#include <stdio.h>
 
int main() {
 
   	int n, horas;
	float vhoras, salario;

	scanf ("%i%i%f", &n, &horas, &vhoras);
	salario = vhoras * horas;
	
	printf ("NUMBER = %i\n", n);
	printf ("SALARY = U$ %.2f\n",salario);
 
    return 0;
}