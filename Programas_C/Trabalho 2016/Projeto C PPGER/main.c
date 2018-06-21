/*
	->DESAFIO PPGER 2016 (Imagem Lena)<-
	
	Dupla: Joao Carlos de Queiroz Prata
		   Eduardo Barros
	
	Curso: Ciencia da Computacao

	Semestre 2015.2

	Fortaleza, 23 de maio de 2016

*/

#include "funcoes.h"

int main(int argc, char **argv){
	if (argc == 2){
		clock_t begin, end;
		double total = 0.0, tm;
		register int i;
		FILE *arquivo;
		FILE *arq;
		FUNCOES_PARA_MATRIZES matrizes;
		IMAGEM img;
		ATRIBUTOS atributos;		

		/* Criacao de arquivo trab.txt */
		if(!(arq = fopen ("trab.txt", "w"))){
		    printf("O arquivo não pode ser criado!\n");
		    exit(1);
		}
	
		/* Abertura do Arquivo */
		if(!(arquivo = fopen (argv[1], "rb"))){
		    printf("O arquivo não pode ser aberto!\n");
		    exit(1);
		}
	
		/* Leitura do cabeçalho do Arquivo */
		ler_cabecalho (&img, arquivo);	
	
		/* Leitura do Arquivo */
		ler_arquivo (&img, arquivo);

		/* Alocação de Matrizes */
		alocar_matrizes (&matrizes, &img, QTIZACAO);
	
		for(i = 0; i < TAM; i++){

			begin = clock();

			/* Quantizar matriz */
			quantizacao(&matrizes, &img, QTIZACAO);

		   	/* Co_ocorrenciar matriz */
			co_ocorrenc (&matrizes, &img, QTIZACAO);  
		
			/* Normalizar matriz */
			normalizar(&matrizes, QTIZACAO);

			/* Energia da Imagem */
			energia(&matrizes, QTIZACAO, &atributos);

			/* Contraste da Imagem */
			contraste(&matrizes, QTIZACAO, &atributos);
		
			/* Homogeneidade da Imagem */
			homogeneidade(&matrizes, QTIZACAO, &atributos);

			/* Correlaçao da Imagem */
			correlacao(&matrizes, QTIZACAO, &atributos);

			end = clock();

			total += (double)(end-begin) / CLOCKS_PER_SEC;

		}

		tm = total/TAM;

		atributos.tempo = tm;

		/* Escrevendo cabecalho, atributos e tempo em um arquivo */
		escrever_arquivo (arq, &atributos);

		/* Desalocandos espaços */
		free(img.pdata);
		free(matrizes.quantizada);
		free(matrizes.co_ocorrenciada);
		free(matrizes.normalizada);
	
		/* Fechando arquivo */
		fclose (arquivo);
		fclose (arq);

		return 0;
	}
	else{
		printf ("Quantidade de argumentos invalida\n");
	}

} 

