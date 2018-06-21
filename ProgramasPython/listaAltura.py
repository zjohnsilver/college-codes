"""
10) Construa um programa que recebe 10 alturas e depois calcula a media das alturas e a altura que
mais se repete.
"""
soma=0
lista=[]
for x in range(10):
	lista.append(float(input("Numero: ")))
	soma+=lista[x]

media=soma/10.0
cont=0
cont2=0
y=lista[0]
for i in range(10):
	if y!=lista[i]:
		y=lista[i]
	cont=cont2
	cont2=0
	for x in range(10):
			if y==lista[x]:
				cont2+=1
		
	if cont2>cont:
		repete=y
print "A media das alturas e",media,"."
print "A altura que mais se repete e",repete,"."
	
				
	