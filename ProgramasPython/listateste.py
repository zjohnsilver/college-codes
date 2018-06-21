lista0 = ["Joao","Casa","Carlos"]
lista1=[]


cont=0
for x in lista0[1]:
	lista1.append(x)
	if cont==1:
		lista1.append("e")
		del(lista1[1])
	cont+=1
	
lista2= [ ]
lista2.append("".join(lista1))	
lista0[1]=lista2
print lista1
print lista2
print lista0

