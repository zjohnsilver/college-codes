#include <stdio.h>

int main(){
	int opcao;
	int VAL;

	printf ("Executar Recebendo ou não valor? (Sim-1/Nao-2)\n");
	scanf("%d", &opcao);

	if (opcao == 1){
		printf ("Valor de VAL:\n");
		scanf ("%d", &VAL);
	}

	else{
		VAL = 1;
	} 

	double A, s, Prec;

	A = 1; s = VAL + A;

	while (s>VAL){
		printf ("Atualização\n\t%f\n\t%f\n", A, s);
		A = A/2;
		s = VAL + A;
	}

	Prec = 2*A;

	printf ("Valor de Prec: %.40f\n", Prec);

	return 0;
}