"""
9) Elabore um programa que leia o nome, custo e preco de 10 produtos e depois mostra os produtos
que tem lucro menor que 10%, os que tem lucro entre 10% e 30% e os que tem lucro maior que
30%. 
"""
lista0 = [ ]
lista1 = [ ]
lista2 = [ ] 
for x in range(10):
	nome=raw_input("Nome: ")
	custo=float(input("Custo: "))
	preco=float(input("Preco: "))
	print " "
	if (preco-custo)/custo<0.1:
		lista0.append(nome)
	elif 0.1<(preco-custo)/custo<0.3:
		lista1.append(nome)
	else:
		lista2.append(nome)
		

print "Produtos com lucro menor que 10%:"
print lista0

print "Produtos com lucro entre 10% e 30%: "
print lista1

print "Produtos com lucro maior que 30%: "
print lista2
	