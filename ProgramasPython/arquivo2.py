test = input("Editar:1 e Ler:2  : ")
if test==1:
	arquivo = open('dados','w')
	lista= [ ]
	for x in range(10):
		lista.append(input("Numero: "))
		arquivo.write(str(lista[x]))
	arquivo.close()
elif test==2:
	arquivo = open('dados','r')

	s=arquivo.read()
	arquivo.close()

	print s
	
else:
	print "Error."
