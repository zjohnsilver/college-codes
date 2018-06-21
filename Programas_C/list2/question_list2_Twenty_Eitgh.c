//
// Escreva um programa que receba dois valores numericos X e Y (unsigned char) e esconda todos os bits de X em cada um dos bits
// menos signiﬁcativos dos 4 elementos imediatamente anteriores e posteriores a Y. (Obs: nao utilizar valores para Y menores que 5).
//
// Created by Jon on 06.03.2016
//


#include <stdio.h>

int main(){
    unsigned char X, Y, valor1, valor2, valor3;
    unsigned int i,z;
    printf ("Valor de X: ");
    scanf ("%c", &X);
    valor1 = X;
    getchar();

    printf ("Valor de Y: ");
    scanf ("%c", &Y);
    valor3 = Y;
    for (i=1; i<=8; i++){
        if (i==5){
            valor3 = Y;
        }
        if (i>=5){
            valor2 = (valor1&1) ^ (valor3+1);
        }
        else{
            valor2 = (valor1&1) ^ (valor3-1);
        }

        printf ("Escondendo o %d bit menos significativo: %c\n", i, valor2);
        valor1>>=1;
        if (i>=5){
            valor3+=1;
        }
        else{
            valor3-=1;
        }

    }

        return 0;
}
