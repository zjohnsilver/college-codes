lista0 = [ "203;Joao;5;9;9" ,"205;Paulo;10;8;7"]
lista1 = [ ]

cont = 0
cont2=0
y=True
for x in lista0[0]:  #Zero e uma variavel que representa a linha que eu encontrar a matricula.
	lista1.append(x)
	if cont==2 and y ==True:
		del(lista1[cont2])
		lista1.append(str(input("Nova nota: ")))
		y=False
	if x==";":
		cont+=1
		print "entrou"
	cont2+=1
print lista1

lista0[0]=lista1

for i in range(2):
	print "".join(lista0[i])
	

