#include <stdio.h>
#include <time.h>
#define MAX 10
#define NL 4
#define NC 5


int main(){
	int matriz[NL][NC], i, *elem = NULL, l, k,j ;
	srand ( (unsigned) time(NULL) );
	elem = matriz[0];
	for (i=0; i< NL*NC; i++){
		*(elem + i) = rand() % MAX;
	}

    printf ("MATRIZ: \n");
    for (i=0; i< NL*NC; i++){
		printf ("%i ", *(elem + i));
		if ((i+1) % NC == 0){
			printf ("\n");
		}
	}

	printf ("\n");
    k = NC-1;
    for (l=0; l<NC/2; l++){
        j = l;
        for (i=0; i< (NL*NC) ; i+=NC){
            printf ("%d -- %d\n",*(elem + j),*(elem + k+j) );
            *(elem + j) = *(elem + j) ^ *(elem + k+j);
            *(elem + k+j) = *(elem + j) ^ *(elem + k+j);
            *(elem + j) = *(elem + j) ^ *(elem + k+j);
            printf ("%d -- %d\n",*(elem + j),*(elem + k+j) );

            j+=NC;
        }
        k-=2;
    }

    printf ("FLIP HORIZONTAL: \n");
    for (i=0; i< NL*NC; i++){
		printf ("%i ", *(elem + i));
		if ((i+1) % NC == 0){
			printf ("\n");
		}
	}

	return 0;
}
