def potencia(a,b):
	resultado=1
	for x in range(b):
		resultado=resultado*a
	return resultado

def raiz(raiz,numero):
	return numero**(1.0/raiz)


print raiz(input("Raiz: "),input("Numero: "))

print potencia(1,0.5)
