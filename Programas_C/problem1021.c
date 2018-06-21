#include <stdio.h>


int main() {
    double valor;
    int cont;
    scanf ("%lf", &valor);
    printf ("NOTAS:\n");
    for (cont=0;valor>=100;cont= cont+1) {
        valor = valor - 100;
    }
    printf ("%i nota(s) de R$ 100.00\n", cont);
    for (cont=0;valor>=50;cont=cont+1) {
        valor = valor - 50;
    }
    printf ("%i nota(s) de R$ 50.00\n", cont);
    for (cont=0;valor>=20;cont=cont+1) {
        valor = valor - 20;
    }
    printf ("%i nota(s) de R$ 20.00\n", cont);
    for (cont=0;valor>=10;cont=cont+1) {
        valor = valor - 10;
    }
    printf ("%i nota(s) de R$ 10.00\n", cont);
    for (cont=0;valor>=5;cont=cont+1) {
        valor = valor - 5;
    }
    printf ("%i nota(s) de R$ 5.00\n", cont);
    for (cont=0;valor>=2;cont=cont+1) {
        valor = valor - 2;
    }
    printf ("%i nota(s) de R$ 2.00\n", cont);

    printf ("MOEDAS:\n");
    for (cont=0;valor>=1;cont=cont+1) {
        valor = valor - 1;
    }
    printf ("%i moeda(s) de R$ 1.00\n", cont);
    for (cont=0;valor>=0.5;cont=cont+1) {
        valor = valor - 0.5;
    }
    printf ("%i moeda(s) de R$ 0.50\n", cont);
    for (cont=0;valor>=0.25;cont=cont+1) {
        valor = valor - 0.25;
    }
    printf ("%i moeda(s) de R$ 0.25\n", cont);

    for (cont=0;valor>=0.10;cont=cont+1) {
        valor = valor - 0.10;
    }
    printf ("%i moeda(s) de R$ 0.10\n", cont);
    printf ("%f\n", valor);
    for (cont=0;valor>=0.05;cont=cont+1) {
        valor = valor - 0.05;

    }
    printf ("%f\n", valor);
    printf ("%i moeda(s) de R$ 0.05\n", cont);

    for (cont=0; valor>=0.01; cont = cont+1){
        valor = valor- 0.01;
    }
    printf ("%f\n", valor);
    printf ("%i moeda(s) de R$ 0.01\n", cont);

    return 0;
}
