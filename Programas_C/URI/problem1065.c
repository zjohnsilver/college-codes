#include <stdio.h>

int main(){
	int cont = 0, i = 5, valor;

	while(i--){
		scanf("%i", &valor);
		if (valor % 2 == 0){
			cont++;
		}
	} 

	printf("%i valores pares\n", cont);

	return 0;
}