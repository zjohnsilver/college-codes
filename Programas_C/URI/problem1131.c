////////////////////////////////////////////
// Problema 1131 URI: Grenais			  //
//                                        //
// Feito por Lancelot                     //
//                                        //
// Data: 16/12/16                         //
////////////////////////////////////////////

#include <stdio.h>

int main(){
	int golsInter, golsGremio, repetir, contador = 0, vitInter = 0, vitGremio = 0, empates = 0; 

	do{
		scanf ("%i %i", &golsInter, &golsGremio);

		if 		(golsGremio > golsInter) vitGremio++;
		else if (golsInter > golsGremio) vitInter++;
		else    empates++;

		printf ("Novo grenal (1-sim 2-nao)\n");
		scanf ("%i", &repetir);

		contador++;
	}while (repetir == 1);

	
	//Estatísticas

	printf ("%i grenais\n", contador);
	printf ("Inter:%i\n", vitInter);
	printf ("Gremio:%i\n", vitGremio);
	printf ("Empates:%i\n", empates);

	if 		(vitInter > vitGremio) printf ("Inter venceu mais\n");
	else if (vitGremio > vitInter) printf ("Gremio venceu mais\n");
	else                           printf ("Nao houve vencedor\n");


	return 0;
}