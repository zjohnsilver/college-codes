#include <stdio.h>

int main(){
	int cont = 0, i = 6;
	double valor;
	
	while(i--){
		scanf("%lf", &valor);
		if (valor > 0){
			cont++;
		}
	} 

	printf("%i valores positivos\n", cont);

	return 0;
}