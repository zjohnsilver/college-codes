////////////////////////////////////////////
// Problema 1009 URI: Salario com Bonus	  //
//                                        //
// Feito por Lancelot                     //
//                                        //
// Data: 11/12/16                         //
////////////////////////////////////////////


#include <stdio.h>

int main(){
	char nome[20];
	double salario_fixo, vendas_dinheiro;

	gets(nome);

	scanf ("%lf%lf", &salario_fixo, &vendas_dinheiro);

	printf ("TOTAL = R$ %.2lf\n", salario_fixo + 0.15*vendas_dinheiro);

	return 0;
}