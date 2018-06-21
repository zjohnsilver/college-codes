#include <stdio.h>

int main(){
    int binario[3];
    unsigned int inteiro, loop=1, mod, i= 0;
    printf ("Numero: ");
    scanf ("%d", &inteiro);
    getchar();
    while (inteiro>0){
        mod = inteiro%2;
        inteiro = inteiro/2;
        binario[i] = mod;
        i+=1;
        printf ("Mod - %d, Inteiro - %d\n", mod, inteiro);
        printf ("%d\n", binario[i]);
    }
    system ("PAUSE");
    return 0;
}
