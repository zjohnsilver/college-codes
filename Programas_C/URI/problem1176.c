////////////////////////////////////////////
// Problema 1176 URI: Fibonnaci em Vetor  //
//                                        //
// Feito por Lancelot                     //
//                                        //
// Data: 11/12/16                         //
////////////////////////////////////////////


#include <stdio.h>

unsigned long long int fibonnaci (int valor);  // É preciso usar long long, pois a precisão de apenas 1 long é 32 bits
											   // E a questão nos pede que seja de 64 bits.

int main(){
	unsigned long int i;
	int qtd_casos, n;

	scanf ("%i", &qtd_casos);

	for (i = 0; i < qtd_casos; i++){

		scanf ("%i", &n);

		printf ("Fib(%i) = %llu\n", n, fibonnaci(n));
	}

	return 0;
}


unsigned long long int fibonnaci (int valor){
	unsigned long long int x, fib1 = 0, fib2 = 1, fib3;

	if (valor<0) return 0;

	for (x = 1; x <= valor; x++){
		fib3 = fib1 + fib2;
		fib1 = fib2;
		fib2 = fib3;
	}

	return fib1; 
}

/* OU TAMBÉM PODE SER FEITO DA SEGUINTE MANEIRA:

#include <stdio.h>

unsigned long int fibonnaci (int valor);

int main(){
	int n, i, qtd_casos;
	unsigned long long int fibonnaci[61] = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
											4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811,
											514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817,
											39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 
											1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 
											20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717,
											365435296162, 591286729879, 956722026041, 1548008755920};

	scanf ("%i", &qtd_casos);

	for (i = 0; i < qtd_casos; i++){

		scanf ("%i", &n);

		printf ("Fib(%i) = %llu\n", n, fibonnaci[n]);
	}

	return 0;
}

*/