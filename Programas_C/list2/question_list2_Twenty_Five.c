//
// Calcular o valor de pi, atraves de uma série inifinita
//
// Created by Jon in 03.03.2016
//

#include <stdio.h>
#include <math.h>


int main() {
    int qtd, i, j=0; // j é a potencia para determinar se o termo da série é positivo ou negativo. j = 0+, j=1-, j=2+
    double pi = 0;

    printf ("Quantidade de Aproximacoes: ");
    scanf ("%d", &qtd);
    // qtd+ j pode ser substituido por qtd + (qtd-1)
    for (i=1; i<=qtd+j; i+=2){ // "qtd + j", Essa é uma relação para se chegar ao valor do denominador. 4 - 4/3 + 4/5,
        pi += 4*pow((-1),j)/i; //Qtd = 1, Denominador = 1, Qtd = 2, denominador = 3, Quantidade = 3, Denominador = 5
        printf ("\nValor de pi com aproximacao de %d termos: %.5lf\n", j+1, pi);
        j+=1;
    }
    printf ("\n");

    system ("PAUSE");
    return 0;
}
