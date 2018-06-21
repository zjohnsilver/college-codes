#include <stdio.h>

int main(){
    register hip, cat1 , cat2;

    for (hip=3; hip<=500; hip++){
        for (cat1=4; cat1<=500; cat1++){
            for (cat2=5; cat2<=500; cat2++){
                if ((hip*hip) == (cat1*cat1) + (cat2*cat2)){
                    printf ("\nHip- %d, Cateto 1- %d, Cateto 2 - %d\n", hip, cat1, cat2);
                    /*printf ("Proximo? 1-Sim, 2 - Encerrar\n");
                    scanf ("%d", &test);*/
                }
            }
        }
    }


    return 0;
}
