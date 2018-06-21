//
// Implementando funcao strstr da biblioteca string.h
//
// Criado por John no dia 29.03.2016
//

#include <stdio.h>
#include <string.h>
 
int strlenght(char str[20]){ // Implementacao da funcao strlen da string.h
	int p = 0, lenght = 0;

	while (str[p] != '\0'){
		lenght += 1;
		p++;
	}
	return lenght;
}

int main(){

	char str[20], str2[10], str3[10];
    int i, j, k=0, total =0, pos[5], pos2, maior = 0;
	
	printf ("String maior: ");
    scanf ("%s", str);

	printf ("String que sera rastreada na maior: ");
    scanf ("%s", str2);

	for (i=0; i<strlenght(str); i++){  // Salvando as posicoes em que esta str2[0] em str
		if (str[i] == str2[0]){
			pos[k] = i;
			k++;
		}
	}

	for (j=0; j < k; j++){ 
		pos2 = pos[j];
		for (i = 0; i < strlenght(str2); i++){ // Laco que salva em str3 uma parte da str.
			str3[i] = str[pos2];
			pos2++;		
		}

		for (i = 0; i < strlenght(str3); i++){ // Laco que compara str3(parte de str) com str2(string para rastrear em str)
			if (str3[i] == str2[i]){
				total+=1; // Variavel incrementa sempre que um caracter de str3 for igual a um caracter de str2
			}
		}
		
		if (total > maior){ // Total pode assumir varios valores, mas o que importa e o maior deles
			maior = total; 
		}
	
		total=0; // Total sempre retorna a zero, para comecar a contagem novamente
	}

	printf ("\n");
	printf ("Total de caracteres iguais: %d\n", maior);

    return 0;
}
