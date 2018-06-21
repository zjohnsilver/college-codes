#include <iostream> // Biblioteca padrão do c++
#include <string>
using namespace std;

int ok (string A, string B, int ta, int tb, int x);

int main(){
	string A[100000];
	string B[10000];
	int ta, tb;
	int e = 0;

	
	getLine(cin, A);
	getLine(cin, B);
	
	ta = A.length();
	tb = B.length();
	
	int d = ta/tb;
	
	while (e<d){
		int m = (e + d) /2;
		
		if (ok(A, B, ta, tb, m)){
			if (ok(A, B, ta, tb, m+1)){
				e = m+1;
			}else{
				cout << "MAX x: " << m << endl;
			}
		}else{
			d = m - 1;
		}
	
	cout << "Max x:" << ok(A, B, ta, tb, e);
	
	
	return 0;
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
