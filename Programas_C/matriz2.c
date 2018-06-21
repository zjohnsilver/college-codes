#include <stdio.h>
#include <time.h>
#define MAX 10
#define NL 4
#define NC 4


int main(){
	int matriz[NL][NC], i, *elem = NULL, s = 0, *ps = NULL, menor;
	srand ( (unsigned) time(NULL) );
	elem = matriz[0];
	ps = &s;
	for (i=0; i< NL*NC; i++){ 
		*(elem + i) = rand() % MAX;
		if (i==0){
			menor = *(elem+i);
		}

		if ((i % (NL+1))==0){
			*ps += *(elem+i);

			if (*(elem+i) < menor){
				menor = *(elem+i);
			}
		}
	}  
	for (i=0; i< NL*NC; i++){
		printf ("%i ", *(elem + i));
		if ((i+1) % NC == 0){
			printf ("\n");
		}		
	}  
	printf ("Soma da diagonal principal: %i\n", *ps);
	printf ("Menor: %i\n", menor);
	
	return 0;
}
