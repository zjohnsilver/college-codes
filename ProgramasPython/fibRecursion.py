def fib(x):
	if x<=0:
		return "Voce digitou um numero que e menor ou igual a zero."
	if x==1 or x==2:
		return 1
	return fib(x-1)+fib(x-2)

n = int(input("Numero: "))

print (fib(n))