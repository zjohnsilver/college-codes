#include "funcoes.c"
int main(){
	Matriz x,y;

	char localA[200];
	char localB[200];

	printf("Entre com o caminho da Matriz A:");
	scanf("%s", localA);
	printf("Entre com o caminho da Matriz B:");
	scanf("%s", localB);

	FILE *A = fopen(localA, "r");
	FILE *B = fopen(localB, "r");

	if(A == NULL && B == NULL){
		printf("Não foi possível abrir o arquivo.\n");
		exit(EXIT_FAILURE);
	}
	
	x = lerMatriz(A);
	y = lerMatriz(B);

	multMatriz(x, y);
	
	fclose(A);
	fclose(B);

	return 0;
}
