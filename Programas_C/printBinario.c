#include <stdio.h>

int binario[100];
int count;

void printBinario(int);
void printBinario2(int);

int main(){
	int num;
	printf ("\t\tCONVERSOR DE DECIMAL PARA BINARIO\n\n");
	printf ("\tInstrucoes\n");
	printf ("Digite um numero para converter\n");
	printf ("Parar a execucao: -1\n\n");
	
	while(1){
		printf ("Numero: ");
		scanf ("%i", &num);
		if (num>=0){
			printBinario2(num);
		}
		else{
			break;
		}
	}
	 
	return 0;
}

void printBinario2(int num){
	int i;
	count = 0;
	printBinario(num);
	
	for (i = count-1; i>=0; i--){
		printf ("%d", binario[i]);
	}
	printf ("\n\n");
}

void printBinario(int num){
	if (num == 1){
		binario[count++] = 1;
		return;
	}
	int resto = num % 2;
	num = num/2;
	
	binario[count++] = resto;
	
	printBinario(num);
}
