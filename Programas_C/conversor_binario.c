#include <stdio.h>


int main() {
	int comparador = 128;
	int decimal;
	int binario;
	
	printf ("\nDecimal: ");
	scanf ("%i", &decimal);
	
	printf ("\nBinario: ");
	while (comparador>0){
		binario = decimal & comparador;
		if (binario){
			printf ("1");
		}
		else{
			printf ("0");
		}
		comparador /=2;
	}
	printf ("\n\n");


	return 0;
}


