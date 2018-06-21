"""
def f1():
	x = 8000
	def f2():
		print (x)
	
	f2()
	
print (f1())
"""

def exp(N):
	def eleva(X):
		print (X**N)
	return eleva			
		
f = exp(3)
x = int(input("Base: "))
print (f(x))


#AULA 40

# Definimos uma função nested, deois atribuimos a f, a função exp com o parâmetro 3, daí, f, fica sendo se referenciando a eleva, 
# como já temos N, só falta X, logo chamando f(2), 2 representará a base, que é o que está faltando.