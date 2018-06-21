def fat(n):
	if n==1 or n==0:
		return 1
	return n*fat(n-1)

def E(x): # x = Quantidade de elementos
	y=1
	for i in range(x-1):
		y=y+1/float((fat(i+1)))
	return y

num = input("Numero: ")

print E(num)

