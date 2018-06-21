def pesoideal(x,y):
	if y=="m" or y=="M" or y== "masculino" or y== "masc" or y == "MASCULINO":
		return 72.7*x-58
	if y == "f" or y == "F" or y == "feminino":
		return 62.1*x - 44.7

altura = input("Altura: ")
sexo = raw_input("Sexo: ")
peso = input("Peso: ")
print "Peso ideal:", pesoideal(altura,sexo)
print ""
if peso<pesoideal(altura,sexo):
	print "Engordar",pesoideal(altura,sexo)-peso,"quilos."
elif peso>pesoideal(altura,sexo):
	print "Emagrecer",peso-pesoideal(altura,sexo),"quilos."