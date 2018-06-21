#include <stdio.h>
#include <math.h>
#include <time.h>
int main()
{
    int n,cont=0,copy_n,copy2_n;
    register i;
    double invert=0;
    scanf("%d",&n);
    copy_n=n;
    copy2_n=n;
    while(copy_n>0){
        cont++;
        copy_n/=10;
    }

    for(i=cont-1;i>=0;i--){
        invert+=(n%10) * pow(10,i);
        n=n/10;
    }

    if(copy2_n==invert){
        printf("e palindromo.\n");
    }
    else{
        printf("nao e palilndromo\n");
    }

    printf("numero invertido:%.0lf\n",invert);

    return 0;
}
