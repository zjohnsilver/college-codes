////////////////////////////////////////////////////////////////
// Problema 1030 URI: A Lenda de Flavious Josephus 			  //
//                                        					  //
// Feito por Lancelot                     					  //
//                                        					  //
// Data: 29/01/2016                       					  //
////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <stdlib.h>

int main(){
		int qtd_casos, qtd_pessoas, tam_salto;
		int *pessoas, cont_mortes, cont_pulos = 0, i, vivo, j = 1;

		scanf ("%i", &qtd_casos);

		while (qtd_casos--){
			scanf ("%i %i", &qtd_pessoas, &tam_salto);

			pessoas = (int *) calloc (qtd_pessoas+1, sizeof(int));

			// Caso não haja espaço na memória para alocar o vetor.
			/*if (!pessoas){
				printf ("Memória insuficiente!\n");

				exit;
			}*/

			cont_mortes = 0, i = 0;

			do{
				while (cont_pulos != tam_salto){
					i++;
					if (i > qtd_pessoas){
						i = 1;
					}

					if (*(pessoas + i) == 0){
						vivo = i;
						cont_pulos++;
					}
				}

				*(pessoas + i) = -1;
				cont_mortes++;
				cont_pulos = 0;
			}while (cont_mortes != qtd_pessoas);



			printf ("Case %i: %i\n", j, vivo);
			j++;

		}

	return 0;
}