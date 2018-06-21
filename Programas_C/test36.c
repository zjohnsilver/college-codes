//
//  aleatorio1.c
//
//
//  Created by Daniel Ferreira on 12/02/15.
//
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define SZ 10000

int main(){
    unsigned int n;

    srand((unsigned int) time(NULL));

    n = rand() % SZ;
    printf ("%u\n", n);
    while (n){
        printf ("%d\n", n%10);
        n/=10;
    }
    return 0;

}
