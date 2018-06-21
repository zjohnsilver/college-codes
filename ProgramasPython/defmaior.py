# Programa que retorna o maior elemento de uma sequência de números.

def maior(nums):
	maior = 0
	for num in nums:
		if num>maior:
			maior = num
	return maior
	
continuar = 1
lista = [ ]

while continuar==1:
	num = int(input("Numero: "))
	lista.append(num)
	continuar = int(input("Continuar - 1, Parar - 2: "))

print ()	
print ("Maior elemento da sequência: ",maior(lista))