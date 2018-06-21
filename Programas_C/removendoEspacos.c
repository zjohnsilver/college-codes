#include <stdio.h>


int main(){
	
	char nome[30] = "  Joao";
	char *str;

	str = nome;


	for (; *str == ''; str++);


	printf ("Nome:%s\n\n", nome);

}