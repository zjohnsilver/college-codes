/*
			### teste.h ###	

	->DESAFIO PPGER 2016 (Imagem Lena)<-
	
	Dupla: Joao Carlos de Queiroz Prata
		   Eduardo Barros
	
	Curso: Ciencia da Computacao

	Fortaleza, 23 de maio de 2016

*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#define QTIZACAO 16
#define TAM 10

typedef struct {
    char codigo[3];
    unsigned int c, l, lum;
    unsigned char *pdata;
}IMAGEM;

typedef struct {
    unsigned char *quantizada;
    unsigned int *co_ocorrenciada;
    double *normalizada;

}FUNCOES_PARA_MATRIZES;

typedef struct {
	double energia;
	double contraste;
	double homogeneidade;
	double correlacao;
	double tempo;

}ATRIBUTOS;

void ler_cabecalho (IMAGEM *img, FILE *arquivo);
void ler_arquivo (IMAGEM *img, FILE *arquivo);
void alocar_matrizes (FUNCOES_PARA_MATRIZES *matrizes, IMAGEM *img, int qtizacao);
void quantizacao (FUNCOES_PARA_MATRIZES *matrizes, IMAGEM *img, int qtizacao);
void co_ocorrenc (FUNCOES_PARA_MATRIZES *matrizes, IMAGEM *img, int dim_ocorrencia);
void normalizar (FUNCOES_PARA_MATRIZES *matrizes, int dimensao);
void energia (FUNCOES_PARA_MATRIZES *matrizes, int dimensao, ATRIBUTOS *atributos);
void contraste (FUNCOES_PARA_MATRIZES *matrizes, int dimensao, ATRIBUTOS *atributos);
void homogeneidade (FUNCOES_PARA_MATRIZES *matrizes, int dimensao, ATRIBUTOS *atributos);
void correlacao (FUNCOES_PARA_MATRIZES *matrizes, int dimensao, ATRIBUTOS *atributos);
void escrever_arquivo (FILE *arq, ATRIBUTOS *atributos);

