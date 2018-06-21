#include <stdio.h>
#include <time.h>
#define MAX 10
#define NL 7
#define NC 7


int main(){
	int matriz[NL][NC], i, *elem = NULL, k = 1;
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
	if (NC%2!=0){
        for (i=0; i< ((NC*NL)-NC)/2 ; i++){
            *(elem + i) =                *(elem + i) ^ *(elem + (i + NL*(NL-k)));
            *(elem + (i + NL*(NL-k) )) = *(elem + i) ^ *(elem + (i + NL*(NL-k)));
            *(elem + i) =                *(elem + i) ^ *(elem + (i + NL*(NL-k)));
            if (i%NC==0 && i!= 0){
                k+=2;
            }
        }

	}
	else{
        for (i=0; i<((NC*NL)/2) ; i++){
            *(elem + i) =                *(elem + i) ^ *(elem + (i + NL*(NL-k)));
            *(elem + (i + NL*(NL-k) )) = *(elem + i) ^ *(elem + (i + NL*(NL-k)));
            *(elem + i) =                *(elem + i) ^ *(elem + (i + NL*(NL-k)));
            if (i%NC==0 && i!= 0){
                k+=2;
            }
        }
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
