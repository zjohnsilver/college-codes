#include <stdio.h>

int main(){
	//Variaveis de lacos for
	int j, x, k;
	//Variaveis envolvendo o losango;
	int qtd_aster=1, largura = 0, altura;

	printf ("Largura do Losango: ");
	scanf ("%i", &altura);

	//Parte de cima do losango
	for (j = 0; j<= altura/2; j++){
		//Apartir da segunda linha ele tem que considerar largura=3
		if (j==1) largura = 3;
		for (x = altura/2; x > j; x--){
			printf (" ");
		}
		for (x = 1; x<=qtd_aster; x++){
			printf ("*");

			for (k = 2; k < largura; k++){
				printf (" ");
			}
		}
		qtd_aster=2;	largura+=2;
		printf ("\n");
	}
	//Parte de baixo do losango
	for (j = 0; j< altura/2; j++){
		//Na ultima lista ele tem que por 1 asterisco apenas
		if (j==(altura/2 - 1)) qtd_aster = 1;

		for (x = 0; x <= j; x++){
			printf (" ");
		}
		for (x = 1; x<=qtd_aster; x++){
			printf ("*");

			for (k = 6; k < largura; k++){
				printf (" ");
			}
		}
		qtd_aster=2;	largura-=2;
		printf ("\n");
	}	
	return 0;
}