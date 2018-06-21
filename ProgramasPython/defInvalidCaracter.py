
def invalidCaracter(z):
	try:
		x = float(input("%s:"%(z)))
		return int(x)
	except:
		print ("Você digitou um caractere inválido.")
		return invalidCaracter(z)
		

b =invalidCaracter("Matricula")
print (b)

		
		