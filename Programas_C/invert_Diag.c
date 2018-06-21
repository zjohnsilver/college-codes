#include <stdio.h>
#include <time.h>
#define MAX 10
#define NL 4
#define NC 4

int main(){
	int matriz[NL][NC], i, *elem = NULL,j, menor;
	srand ( (unsigned) time(NULL) );
	elem = matriz[0];
	j = (NC+1)*(NC-1);
	for (i=0; i< NL*NC; i++){
		*(elem + i) = rand() % MAX;

	}
	for (i=0; i< NL*NC; i++){
		printf ("%i ", *(elem + i));
		if ((i+1) % NC == 0){
			printf ("\n");
		}
	}
	printf ("\n\n");
	for (i=0; i< (NL*NC)/2; i+=(NC+1)){
		*(elem+i) = *(elem+i)^*(elem+j);
		*(elem+j) = *(elem+i)^*(elem+j);
		*(elem+i) = *(elem+i)^*(elem+j);
		j -= NC+1;


	}
	for (i=0; i< NL*NC; i++){
		printf ("%i ", *(elem + i));
		if ((i+1) % NC == 0){
			printf ("\n");
		}
	}

	return 0;
}
