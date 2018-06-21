#Criando uma Matriz 3 x 2:

matriz = []


for x in range(3):
	matriz.append([])

for x in range(3):
	for i in range(2):
		matriz[x].append(input("Linha %i e coluna %i :"%(x,i)))


for i in range(3):
	print matriz[i]
print "\n"
print "ou"

print matriz