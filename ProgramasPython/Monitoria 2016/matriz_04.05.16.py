
def TOTAL (matriz, linha, coluna):
	soma = 0
	for x in range(linha):
		for y in range(coluna):
			soma += matriz[x][y]
			
	return soma


def mostrar_matriz (matriz, linha, coluna):
	print ("\tP1\tP2\tP3\tP4\tP5")
	for x in range(linha):
		print "V%i "%(x+1),
		for y in range(coluna):
			print "\t",matriz[x][y],
		print ""
	
def soma_coluna (matriz, linhas, coluna_somar):
	soma = 0
	for x in range(linhas):
		soma += matriz[x][coluna_somar]
		
	return soma		
		
def soma_linha (matriz, linha_somar, colunas):
	soma = 0
	for x in range(colunas):
		soma += matriz[linha_somar][x]
		
	return soma


def main():
	matriz = []	
	for x in range(3):
		matriz.append([])
		for y in range(5):
			matriz[x].append(0)
			
	while True:	
		print ("\nMENU:")
		print ("1 - Entrar com um produto: ")
		print ("2 - A quantidade de vendas de cada tipo de produto")
		print ("3 - A quantidade de vendas de cada vendedor")
		print ("4 - Quantidade Total")
		print ("5 - Matriz de vendas")
		print ("6 - SAIR ")	

		opcao = input ("Opcao-> ")
		print ("")
		
		if (opcao == 1):
			print ("Produtos: 1, 2, 3, 4, 5")
			produto = input ("\tProduto: ")
			vendedor = input ("\tVendedor 1, 2 ou 3: ")
			matriz[vendedor-1][produto-1] +=1
			
		if (opcao == 2):
			print ("Vendas de cada produto: ")	
			
			for x in range(5):
				print ("Produto %i: %i" %(x+1, soma_coluna (matriz, 3, x)))
				
		if (opcao==3):
			print ("Vendas de cada vendedor: ")
			
			for x in range(3):
				print ("Vendedor %i: %i" %(x+1, soma_linha (matriz, x, 5)))
				
		if (opcao == 4):
			print ("TOTAL de Vendas: ")
			
			print ("TOTAL: %i" %(TOTAL (matriz, 3, 5))) 		

		if (opcao == 5):
			print ("Matriz de vendas: ")
			mostrar_matriz (matriz, 3, 5)
			
		if (opcao==6):
			print ("---------PROGRAMA ENCERRADO---------")
			break

	
main()	
		
	




