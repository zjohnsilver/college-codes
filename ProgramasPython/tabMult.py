# Tabela de Multiplicação

print("Um Número só tem inverso, quando é primo com determinado resto. \n")

modulo = int(input("Digite o módulo da Tabela de Multiplicação: "))
for linha in range(1,modulo):
	print ("Linha: ",linha)
	for coluna in range(1,modulo):
		if linha *coluna <= modulo:
			if linha*coluna ==1:
				print ("%ix%i = 1"%(linha,coluna))
		elif linha *coluna >modulo:
			if (linha*coluna)% modulo == 1:
				print("%ix%i = 1"%(linha,coluna))
	
	