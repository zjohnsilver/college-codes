//
//  overflowTipo.c
//
//  Objetivo: Check overflow em variavel.
//
//  Created by Daniel Ferreira on 2/3/16.
//
//

#include <stdio.h>
#include <unistd.h>

unsigned int somar(unsigned int a, unsigned int b){
    unsigned int r;
    r = a + b;
    return r;
}


int main(){

    unsigned int x = 429496, i;

    for (i=0;i<20;i++) {
        printf("%u\n",somar(x,i));
        _sleep(1000);  // Usar _sleep no windows, e apenas sleep no linux e Mac;
    }

    return 0;

}
