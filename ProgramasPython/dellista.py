lista = []

tam = int(input("Tamanho da Lista: "))

for x in range(tam):
	lista.append(int(input("Numero: ")))
print lista

x = float(input("Eliminar da Lista: "))
y=0
while y<tam: 
	if x==lista[y]:
		del(lista[y])
		tam=tam-1
		y=y-1
	y=y+1

print (lista)