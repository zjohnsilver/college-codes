from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
	print ("fib(%d)" %(n))
	if n<=2:
		return 1
	return fib(n-1) + fib(n-2)


print (fib(int(input("Digite um Número: "))))