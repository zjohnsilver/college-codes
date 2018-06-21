#include <stdio.h>

int main(){
    float num, denom;
    printf ("Numerador: ");
    scanf ("%f", &num);
    do{
        printf ("Denominador: ");
        scanf ("%f", &denom);

    }while (denom==0);

    printf ("Divisao: %.2f\n", num/denom);

    system("PAUSE");
    return 0;
}
