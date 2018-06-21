# Função recursiva que printa os valores de x a y

def printx_y(x,y):
	if x==y:
		return print (x)
	return print (x),printx_y(x+1,y)
	


# Função recursiva que soma todos os valores até n
def soma(n):
	if n ==1:
		return 1
	return n+soma(n-1)
	
print (soma(6)) 