#include <stdio.h>
#include <stdlib.h>

// Programa que resolve uma multiplicao, como uma soma sucessiva.
// Porem so esta funcionando para multiplicacao de numeros com 1 algarismo

int count = 0;
int num1, num2;

int somaSucessivas(int);

int main(){
	char operacao[10];
	
	scanf ("%s", operacao);
	
	num1 = atoi(&operacao[0]);
	num2 = atoi(&operacao[2]);
	
	printf ("%d\n\n", somaSucessivas(num2));
	
	return 0;
}

int somaSucessivas(int num){
	if (count == num1){
		return 0;
	}
	else{
		count++;
		return num + somaSucessivas(num);
	}
}
