#include <stdio.h>

int main(){
	int vetor[20], i;
	int ultIndex = 19;

	for (i = 0; i<20; i++){
		scanf("%i", &vetor[i]);

	}

	for (i = 0; i<10; i++){
		vetor[i] = vetor[i] ^ vetor[ultIndex];
		vetor[ultIndex] = vetor[i] ^ vetor[ultIndex];
		vetor[i] = vetor[i] ^ vetor[ultIndex];

		ultIndex -=1;
	}

	for (i = 0; i<20; i++){
		printf ("N[%i] = %i\n", i, vetor[i]);

	}


	return 0;
}
