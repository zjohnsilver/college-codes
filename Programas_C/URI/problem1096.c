#include <stdio.h>

int main(){
	int i, j;

	for (i = 1; i<10; i+=2){
		for (j = 7; j>4; j--){
			printf ("I=%i J=%i\n", i, j);
		}
	}

	return 0;
}