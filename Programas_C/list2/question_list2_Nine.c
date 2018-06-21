//
//Serie de Fibonnaci
//
//Created by Jon in 02.03.2016
//
#include <stdio.h>

int main(){
    int fib1=1, fib2=1,i, fib3;
    printf ("SERIE DE FIBONNACI\n")
    for (i=0;i<20;i++){
        printf ("%d - ", fib1);
        fib3=fib1+fib2;
        fib1=fib2;
        fib2=fib3;
    }

    system("PAUSE");

    return 0;
}
