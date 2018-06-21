############################################
## Fibonacci, Quantas Chamadas?
## Para a solução ser aceita, eu rodei o programa com as respostas, e armzenei tudo em listas.
## Antes de fazer isso, estava dando erro Time Limit Exceeded
## URI ONLINE - Problema 1029 - Iniciante
##
## Created by Jon in 19.06.2016
##	
## Python 3


def calls(n):
	if n==0:
		return 1
	elif n==1:
		return 1

	return calls(n-1) + calls(n-2) + 1

def fib(n):
	if n==0:
		return 0
	elif n==1:
		return 1

	return fib(n-1) + fib(n-2)


# Casos de teste
qtd_testes = int(input())

for y in range(qtd_testes):
	valor = int(input())

	print ("fib(%d) = %d calls = %d" %(valor, calls(valor) - 1, fib(valor)))