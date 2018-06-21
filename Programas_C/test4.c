#include <stdio.h>

int main()
{
    char s;
    float a;
    float c;

    printf ("Informe sua altura em metros:");
    scanf ("%f",&a);
    getchar();
    printf("Informe o seu sexo (M)Masculino ou (F)Feminino\n");
    scanf("%c", &s);
    printf ("%c", s);
    if (s=='M') {
        c= 72.7*a-58;
        printf("Seu peso ideal(M) e: %f ",c);
    }
    else if (s=='F') {
        c=62.1*a-44.7;
        printf("Seu peso ideal(F) e:% f ",c);
        }
    else {
        printf("invalido");
    }


    return 0;
}
