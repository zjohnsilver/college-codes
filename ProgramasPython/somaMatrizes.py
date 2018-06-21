#Soma de Matrizes

matrizx = [[],[],[]]
matrizy = [[],[],[]]
matrizsoma = [[],[],[]]


for x in range(3):
	print 
	for i in range(2):
		matrizx[x].append(input("Linha %i e Coluna %i: "%(x,i)))
		matrizy[x].append(input("Linha %i e Coluna %i: "%(x,i)))



for x in range(3):
	for i in range(2):
		matrizsoma[x].append(matrizx[x][i] + matrizy[x][i])


print "Soma das Matrizes \n   %s \n   %s\n\n = %s."%(matrizx,matrizy,matrizsoma)


