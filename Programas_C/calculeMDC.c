#include <stdio.h>
/*Programa que Calcula o MDC de dois números.*/
int number5;
int main(){
    int number1, number2, number5;
    puts ("Numeros para o calculo do MDC. Ex: 20 30");
    scanf ("%d%d", &number1, &number2);
    if (number1<number2){
        number1 = number1^number2;
        number2 = number1^number2;
        number1 = number1^number2;
    }
    number5 = mdc(number1,number2);
    printf ("MDC entre %i e %i e %i.", number1, number2, number5);

    return 0;
}
/*Funcao que calcula o mdc*/
int mdc(int x, int y){
    while (x%y){
        number5 = x;
        x = y;
        y = number5%y;
    }
    return y;
}

