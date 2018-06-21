lista = [1,2,-1,4]
lista2 = [-2,6,7,8]



def cont(x):
	x.append("")
	test=True
	i=0
	cont=0
	while test==True:
		if x[i]  != "":
			cont+=1
		else:
			test=False
		i+=1
	return cont
def ordem(x,y):
	new = [ ]
	menor = x[0]
	for j in range(cont(x)+cont(y)):
		for i in range(1,cont(x)):
			if x[i] < m
				menor = x[i]
		for i in range(0,cont(y)):
			if y[i]<menor:
				menor = y[i]
		new.append(menor)
	print new
	
	
print ordem(lista,lista2)
	
	