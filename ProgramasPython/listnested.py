def lista():
	start = 0
	lista = [ ]
	def incrementa(item):
		nonlocal lista, start
		lista.append(item)
		start += 1
		print (item, start)
	return incrementa
	
compras1 = lista()   # Necessário atribuir a variável compras1, a função lista(). A maneira como eu entendi: Ela não tem argumentos, logo, atribuimos ela a variável compras1, e assim compras1 tem um argumento,
							# Que é o argumento "ITEM" da segunda função.

compras1('presunto')
compras1("pão")
compras1("carrapato")