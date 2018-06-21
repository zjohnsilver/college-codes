#include <stdio.h>

int main() {
    int z= 0;
    char linha[100];
    char ch;
    unsigned int y =4294967295;
    signed int x = -(4294967295/2);
    unsigned short int w =65535;
    //w = x^w; 0000 1010
    //x = x^w;
    //w = x^w;
    printf ("Z= %i,%i, Y= %lu,%lu, X=%i,%i W=%i,%i\n", sizeof(z),z,sizeof(y),y,sizeof(x),x, sizeof(w),w);
    printf ("Digite uma string:\n");
    do {
         ch = getchar();
         linha[z] = ch;
         ++z;
    } while(ch!= '\n');
    linha[z-1] = '\0';

    printf ("String Digitada: %s\n", linha);
    printf ("Ultimo caractere lido: %c.\n", ch);
    return 0;
}
