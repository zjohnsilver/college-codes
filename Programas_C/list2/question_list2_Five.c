#include <stdio.h>

int main(){
    int n, maior, menor;
    printf ("Numero: ");
    scanf ("%d", &menor);
    maior = menor;
    do{
        printf ("Numero: ");
        scanf ("%d", &n);
        if (n!=0){
            if (n>maior){
                maior=n;
            }
            if (n<menor){
                menor=n;
            }
        }

    }while(n!=0);
    printf ("Maior: %i, Menor: %i.\n", maior, menor);

    return 0;
}
