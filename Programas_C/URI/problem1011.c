////////////////////////////////////////////
// Problema 1011 URI: Esfera			  //
//                                        //
// Feito por Lancelot                     //
//                                        //
// Data: 11/12/16                         //
////////////////////////////////////////////


#include <stdio.h>
 
int main() {
 
    int R;
    double volume, pi = 3.14159;

    scanf ("%d", &R);
    volume = (4/3.0) * pi * R * R * R;
    
    printf ("VOLUME = %.3f\n", volume);
 
    return 0;
}