// Criado em 16-04-17 por Lancelot

// Lógica do programa:
//
// Somar os pesos dos painéis
// Dividir esse valor da quantidade de caminhões para obter uma media que cada um deve carregar.
// Em seguida calcular a margem de peso que cada um pode levar: Peso_total/ (qtd_paineis*2)
// Subtrair a media da margem de erro, e o resultado usar como parâmetro para escolher os paineis que vão em cada caminhão



#include <stdio.h>
#include <stdlib.h>


int main(){
	int qtd_testes, nPaineis, caminhoes, valor_frete, peso_total, temp, frete_total;
	int *caminhao, *pesos;
	int media, maior = 0;

	int i, j;

	scanf("%d", &qtd_testes);

	while (qtd_testes--){
		scanf ("%d%d%d", &nPaineis, &caminhoes, &valor_frete);

		caminhao = (int*) calloc(caminhoes, sizeof(int));
		pesos = (int*) (malloc(nPaineis*sizeof(int)));

		
		i = 0;
		peso_total = 0;
		while (i<nPaineis){
			scanf("%d", &temp);

			*(pesos + i) = temp;

			peso_total+=temp; 
			i++;
		}

		//Calculo da media de peso que cada um pode carregar
		media = (peso_total/caminhoes);

		printf ("Media: %d\n", media);

		i = 0, j = 0;
		while ((i < caminhoes) && (j < nPaineis)){
			if (*(caminhao + i) < (media+ 20)){ //Enquanto o caminhao ainda nao tiver atingido a media, ele adiciona valores a ele
										  //Ideia: Poderia ser substituido por um while... ver isso depois.
				*(caminhao + i) += *(pesos + j);
				j++;

				if (*(caminhao+i) > maior){
					maior = *(caminhao + i);
				}

				printf ("Peso caminhao %d: %d\n", (i+1), *(caminhao + i));
			}

			if ((*(caminhao + i) >= media) || (*(caminhao +i) > (media-10)))  { //Entra aqui quando for para passar para o PROXIMO caminhao
				i++;
			}
		}

		frete_total = caminhoes * maior * valor_frete; //qtd_caminhoes * carga_mais_pesada * valor_frete

		printf ("%d $%d\n", maior, frete_total);

		
	}	


	return 0;
}