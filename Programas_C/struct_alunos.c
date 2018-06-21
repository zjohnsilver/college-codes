#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define NOTA 11
#define MAT 10000
#define QTD 10

//Struct
struct alunos{
	int N1, N2, N3;
	float M;
	unsigned int matricula;

};

//Prototipo das funcoes
void calcular_media (struct alunos *pAlunos);

int main(){

	int i, qtd_alunos;

	struct alunos *student;

	printf ("Quantidade de Alunos: ");
	scanf ("%d", &qtd_alunos);

	//Alocando dinamicamente a quantidade de alunos
	student = (struct alunos *) malloc (qtd_alunos * sizeof (struct alunos));   

	//Semente para a funcao rand();
	srand ((unsigned) time(NULL));

	//Laco que percorre a struct
	for (i = 0; i<QTD; i++){

		//Gerando notas aleatoriamente
		student[i].N1 = rand() % NOTA;
		student[i].N2 = rand() % NOTA;
		student[i].N3 = rand() % NOTA;
		student[i].matricula = rand() % MAT;
		calcular_media (student + i); /* Chamando a funcao com o endereço de cada posição do struct */

		printf ("Aluno: %i\n", i+1);
		printf ("\tMatricula: %i\n", student[i].matricula);
		printf ("\tN1: %i\n", student[i].N1);
		printf ("\tN2: %i\n", student[i].N2);
		printf ("\tN3: %i\n", student[i].N3);
		printf ("\tMedia: %.2f\n\n", student[i].M);
	}

	return 0;
}

//Funcao que calcula a media;
void calcular_media (struct alunos *pAlunos){
	int i;

	//Acessando valores da struct
	(*pAlunos).M = ((*pAlunos).N1 + (*pAlunos).N2 + (*pAlunos).N3) / 3.0;
}
