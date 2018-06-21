#include <stdio.h>

int main(){
    int alt_Jose = 150, alt_Pedro = 110, anos=0;
    while (alt_Jose>alt_Pedro){
        alt_Jose+=2;
        alt_Pedro+=3;
        anos+=1;
    }
    printf ("Em %i anos Pedro sera maior que Jose.\n", anos);

    return 0;
}
