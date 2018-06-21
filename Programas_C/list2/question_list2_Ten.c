//
// Quadrado dos multiplos de 4, na faixa [15,90]
//
//Created by Jon in 02.03.2016
//

#include <stdio.h>

int main(){
    int j;
    for (j=15; j<=90;j++){
        if (!(j%4)){
            printf ("Quadrado de %i : %i\n", j, j*j);
        }
    }

    system ("PAUSE");
    return 0;
}
