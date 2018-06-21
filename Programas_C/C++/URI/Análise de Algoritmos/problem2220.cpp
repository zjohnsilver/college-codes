#include <iostream> // Biblioteca padrão do c++
#include <string>
#include <sstream>

using namespace std;

int ok (string A, string B, int ta, int tb, int x);
int buscaBinaria(string A, string B, int ta, int tb);

int main(){
	int N;
	int ta, tb;
	string A = "";
	string B = "";

	cin >> N;
	
	while (N--){
		cin >> A;
		cin >> B;
		
		ta = A.length();
		tb = B.length();
		
		int resposta = buscaBinaria(A, B, ta, tb);
		
		cout << resposta <<  endl;

	}
	return 0;
}

int buscaBinaria(string A, string B, int ta, int tb){
	int e = 0;
	int d = ta/tb;
	
	while (e < d){
		int m = (e+d)/2;
		
		if (ok(A, B, ta, tb, m) == 1){
			if (ok(A, B, ta, tb, m+1) == 1){
				e = m + 1;
			}else
				return m;
			
		}else{
			d = m - 1;
		}		
		
		
	}
	
	return e;
}


int ok (string A, string B, int ta, int tb, int x){
	int match = 0;
	int b = 0;
	
	if (x == 0){
		return 1;
	}
	
	for (int a = 0; a < ta; a++){
		if (A[a] == B[b]){
			match++;
		}
		
		if (match == x){
			b++;
			match = 0;
		}
		
		if (b == tb){
			return 1;
		}
	} 
	
	return 0;
}
