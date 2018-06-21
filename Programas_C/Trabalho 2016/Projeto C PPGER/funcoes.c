/*
			### teste.c ###	

	->DESAFIO PPGER 2016 (Imagem Lena)<-
	
	Dupla: Joao Carlos de Queiroz Prata
		   Eduardo Barros
	
	Curso: Ciencia da Computacao
	
	Semestre 2015.2

	Fortaleza, 23 de maio de 2016

*/

#include "funcoes.h"

void ler_cabecalho (IMAGEM *img, FILE *arquivo){

	fscanf (arquivo, "%s %u %u %u", img->codigo, &img->c, &img->l, &img->lum);

}

void ler_arquivo (IMAGEM *img, FILE *arquivo){
	
	/*Posicinando o ponteiro antes do primeiro valor a ser lido: 133...*/
	fseek (arquivo, 1, SEEK_CUR);

	img->pdata = (unsigned char *) malloc (img->c*img->l* sizeof(unsigned char));
	
	if (!(img->pdata)){
		exit(1);
	}

	fread (img->pdata, sizeof(unsigned char), img->c*img->l, arquivo);
}

void alocar_matrizes (FUNCOES_PARA_MATRIZES *matrizes, IMAGEM *img, int qtizacao){

    
    if (!(matrizes->quantizada = (unsigned char *) malloc (img->c*img->l* sizeof(unsigned char))) || 
		!(matrizes->co_ocorrenciada = (unsigned int *) calloc (qtizacao*qtizacao, sizeof(unsigned int))) || 
		!(matrizes->normalizada = (double *) malloc (qtizacao*qtizacao* sizeof(double)))){

		puts ("Sem memoria suficiente!!!");
        exit(1);
    }
}
 
void quantizacao (FUNCOES_PARA_MATRIZES *matrizes, IMAGEM *img, int qtizacao){
    register int i;
 
    for (i=0; i < (img->l*img->c); i++){
        *(matrizes->quantizada + i) = *(img->pdata + i)/ qtizacao;
    }
}

void co_ocorrenc (FUNCOES_PARA_MATRIZES *matrizes, IMAGEM *img, int dim_ocorrencia){
    register int i;
 
    for (i=0; i<img->l*img->c; i++){
        if ((i+1)%img->c){
            /* Maneira de percorrer uma matriz, usando linha e coluna, com ponteiro.
              ----> *(ponteiro + (NC*linha + coluna));  NC*linha + coluna*/
            matrizes->co_ocorrenciada[( dim_ocorrencia * *(matrizes->quantizada+i) + *(matrizes->quantizada+(i+1)) )] +=1;
        }
    }
}
 
void normalizar (FUNCOES_PARA_MATRIZES *matrizes, int dimensao){
    register int i;
    float somatorio = 0;
 

    for (i=0; i<dimensao*dimensao; i++){
        somatorio += *(matrizes->co_ocorrenciada + i);
    }
 	
    for (i=0; i<dimensao*dimensao; i++){
        *(matrizes->normalizada + i) = *(matrizes->co_ocorrenciada + i) /somatorio;
    }
 
}

/*Somatorio (matriz(i,j))^2*/
void energia (FUNCOES_PARA_MATRIZES *matrizes, int dimensao, ATRIBUTOS *atributos){
	register int i;
	float energy = 0.0;

	for (i = 0; i < dimensao*dimensao; i++){
		energy += *(matrizes->normalizada + i)**(matrizes->normalizada + i);
	}
	
	/* Manda atributo na struct */
	atributos->energia = energy;
}

/*Somatorio ((|i-j|^2)*matriz(i,j))*/
void contraste (FUNCOES_PARA_MATRIZES *matrizes, int dimensao, ATRIBUTOS *atributos){
	register int i, j;
	float contrast = 0.0;

	for (i = 0; i < dimensao; i++){
		for (j = 0; j < dimensao; j++){
			contrast += ((i-j)*(i-j)) * *(matrizes->normalizada + (dimensao*i + j));
		}
	}
	
	/* Manda atributo na struct */
	atributos->contraste = contrast;
}

/*Somatorio (matriz(i,j)/(1+|i-j|))*/
void homogeneidade (FUNCOES_PARA_MATRIZES *matrizes, int dimensao, ATRIBUTOS *atributos){
	register int i, j;
	float homogene = 0.0;

	for (i = 0; i < dimensao; i++){
		for (j = 0; j < dimensao; j++){
			homogene += *(matrizes->normalizada +(dimensao*i + j))/ (1+abs(i - j)) ;
		}
	}
	
	/* Manda atributo na struct */
	atributos->homogeneidade = homogene;
}

/*Somatorio ((i - ui) * (j - uj) * matriz(i, j))/ (ai*aj)
  Entenda o somatorio com os comentarios na funcao */
void correlacao (FUNCOES_PARA_MATRIZES *matrizes, int dimensao, ATRIBUTOS *atributos){
	register int i, j;
	float correlacao , ui, uj, ai, aj;

	correlacao = ui = uj = ai = aj = 0.0;

	for (i = 0; i < dimensao; i++){
		for (j = 0; j < dimensao; j++){
			ui += i**(matrizes->normalizada + (dimensao*i + j)); /*Somatorio (i * matriz(i,j))*/
			uj += j**(matrizes->normalizada + (dimensao*i + j)); /*Somatorio (j * matriz(i,j))*/
		}
	}

	for (i = 0; i < dimensao; i++){
		for (j = 0; j < dimensao; j++){
			ai += *(matrizes->normalizada + (dimensao*i + j)) * ((i-ui)*(i-ui)); /*Somatorio (matriz(i,j) * |i-ui|^2)*/
			aj += *(matrizes->normalizada + (dimensao*i + j)) * ((j-uj)*(j-uj)); /*Somatorio (matriz(i,j) * |j-uj|^2)*/
		}
	}

	ai = sqrt(ai); /*Tirando raiz quadrada do somatorio ai*/
	aj = sqrt(aj); /*Tirando raiz quadrada do somatorio aj*/

	for (i = 0; i < dimensao; i++){
		for (j = 0; j < dimensao; j++){
			correlacao += ( ((i-ui)*(j-uj)) * *(matrizes->normalizada + (dimensao*i + j) ) ) / (ai*aj);
		}
	}
	
	/* Manda atributo na struct */
	atributos->correlacao = correlacao;
}

void escrever_arquivo (FILE *arq, ATRIBUTOS *atributos){
	
	fprintf (arq, "\t\t\t### DESAFIO PPGER ###\n\n");
	fprintf (arq, "\tDupla:  Joao Carlos de Queiroz Prata\n");
	fprintf (arq, "\t\t\t\tMatricula: 20151045050465\n\n");
	fprintf (arq, "\t\t\tEduardo Mariano de Barros\n");
	fprintf (arq, "\t\t\t\tMatricula: 20151045050384\n\n");
	fprintf (arq, "\tCurso: Ciencia da Computacao\n\n");
	fprintf (arq, "\tProfessor: Daniel Silva\n\n");
	fprintf (arq, "\tData: 23 de Maio de 2016\n\n");
	fprintf (arq, "\tATRIBUTOS: \n");
	fprintf (arq, "\t\tEnergia:\t\t%.4lf\n", atributos->energia);
	fprintf (arq, "\t\tContraste:\t\t%.4lf\n", atributos->contraste);
	fprintf (arq, "\t\tHomogeneidade:\t%.4lf\n", atributos->homogeneidade);
	fprintf (arq, "\t\tCorrelacao:\t\t%.4lf\n\n", atributos->correlacao);
	fprintf (arq, "\tTEMPO:\t%lf \n", atributos->tempo);

}


