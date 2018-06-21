#include <stdio.h>
#include <string.h>

void medir_string (const char *const str, int *const pdata);

int main(){
	char str2[200];
	int vetor[3] = {0, 0, 0}, x;
	
	printf ("String: ");
	fgets (str2, sizeof(str2), stdin);

	medir_string (str2, &vetor[0]);
	
	str2[strlen(str2)-1] = ' ';
	printf ("Informações da frase: { %s} ", str2);
	printf ("\n\tPalavras: %d", vetor[0]);
	printf ("\n\tCaracteres: %d", vetor[1]);
	printf ("\n\tLinhas: %d\n", vetor[2]);

	return 0;
}


void medir_string (const char *const str, int *const pdata){
	int i;
	 *(pdata) = 1; 
	
	// Contando numero de palavras
	for (i=0; i<strlen(str); i++){
		if (str[i] == ' '){
			*(pdata)+=1;
		}
	}
	
	// Numero de caracters	
	*(pdata+1) = strlen(str)-1;

	//Numero de linhas
	for (i=0; i<strlen(str); i++){
		if (str[i] == '\n'){
			*(pdata+2)+=1;
		}
	}		
}


