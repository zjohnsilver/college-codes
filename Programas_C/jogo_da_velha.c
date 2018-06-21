#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10

void mostrar_tabuleiro(int *matriz);
void pegar_jogada(int *matriz, int *jogador);
void verifica_vencedor (int *matriz, char *vitoria);

int main(){
	char vitoria = ' ';
	int x=0, i, *matriz = NULL;

	matriz = (int *) malloc (9 * sizeof(int));

	//Preenchendo matriz
	for (i=0; i<9; i++){
		*(matriz + i) =  i;
	}

	printf ("\n*******JOGO DA VELHA*******\n");
	printf ("Digite o numero correspondente ao espaço.\n\n");

	while (vitoria == ' '){
		mostrar_tabuleiro (matriz);
		pegar_jogada (matriz, &x);
		verifica_vencedor(matriz, &vitoria	);
	}


	printf ("\nVOCE GANHOU!!!\n");
	mostrar_tabuleiro (matriz);
	printf ("\n");

	getchar();
	getchar();

	return 0;
}

void mostrar_tabuleiro(int *matriz){
	int i, j;

	for (i=0; i<3; i++){
		for (j=0; j<3; j++){
			if (j!=2){
				if (*(matriz + (3*i +j)) == -1){
					printf (" X |");
				}
				else if (*(matriz + (3*i +j)) == -2){
					printf (" O |");
				}
				else{
					printf (" %d |", *(matriz + (3*i + j)));
				}
			}
			else{
				if (*(matriz + (3*i +j)) == -1){
					printf (" X ");	
				}
				else if (*(matriz + (3*i +j)) == -2){
					printf (" O ");
				}
				else{
					printf (" %d ", *(matriz + (3*i + j)));
				}
			}
		}
		if (i!=2){
			printf ("\n___|___|___\n");	
		}
		else{
			printf ("\n   |   |\n");			
		}
	}

}

void pegar_jogada(int *matriz, int *jogador){
	int valor;

	printf ("\nValor: ");
	scanf ("%d", &valor);

	if (!(*jogador % 2)){ //Se for par
		*(matriz + valor) = -1;		
	}
	else{                 //Se for impar
		*(matriz + valor) = -2;		
	}
	(*jogador) ++;

}

void verifica_vencedor (int *matriz, char *vitoria){

	if   ((*(matriz + 0) == *(matriz + 4) && *(matriz + 0) == *(matriz + 8)) || (*(matriz + 2) == *(matriz + 4) && *(matriz + 2) == *(matriz + 6))){
		*vitoria = '-';
	}
	else if ((*(matriz + 0) == *(matriz + 1) && *(matriz + 0) == *(matriz + 2)) || (*(matriz + 3) == *(matriz + 4) && *(matriz + 3) == *(matriz + 5))){
		*vitoria = '-';
	}
	else if ((*(matriz + 6) == *(matriz + 7) && *(matriz + 6) == *(matriz + 8)) || (*(matriz + 0) == *(matriz + 3) && *(matriz + 0) == *(matriz + 6))){
		*vitoria = '-';
	}
	else if ((*(matriz + 1) == *(matriz + 4) && *(matriz + 1) == *(matriz + 7)) || (*(matriz + 2) == *(matriz + 5) && *(matriz + 2) == *(matriz + 8))){
		*vitoria = '-';
	}
}
