#8) Faca um programa que recebe os elementos de uma lista com 10 inteiros. O programa tambem deve mostrar os numeros primos e suas respectivas posicoes.

def primo(n):
	cont=0
	for x in range(2,n):
		if n%x==0:
			cont+=1
	
	if cont==0:
		return True
	else:
		return False
		

		
lista = [ ]

for x in range(10):
	lista.append(int(input("Numero: ")))
	
for x in range(10):
	if primo(lista[x])==True:
		print ("O numero",lista[x], "e primo e esta na posicao",x,"da lista.")
