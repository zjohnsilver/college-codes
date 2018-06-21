# Faca um programa que leia 10 valores e coloque em uma lista. Depois, mostre quais elementos da lista estao repetidos e quantas vezes cada um se repete.


lista = [ ] 


for x in range(10):
	lista.append(input("Numero: "))

hello=0
listarepeat= [ ]
for x in range(10):
	z=lista[x]
	cont=1
	k=0
	contrepeat=0
	for w in range(hello):
		if lista[x]!=listarepeat[w]:
			contrepeat+=1
	if contrepeat==hello:
		k=1
	if x==0 or k==1:
		for y in range(10):
			if lista[x]==lista[y] and x!=y:
				cont+=1
		listarepeat.append(z)
		hello+=1

		print "%i se repete %i vezes."%(z,cont) 


