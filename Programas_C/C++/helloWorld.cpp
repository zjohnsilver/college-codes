#include <iostream>

using namespace std;

int main(){
	int i;
	string nome;

	cout << "Nome: ";
	cin >> nome;

	cout << "Hello World" << endl;

	for (int j = 0; j<10 ; j++){
		cout << "Valor " << nome << endl;
		i++;
	}

	return 0;
}