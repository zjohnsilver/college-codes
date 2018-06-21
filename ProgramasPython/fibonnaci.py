#Programa Fibonnaci

fib1 = 1
fib2 = 1

print " *****MENU***** "
print " 1 - Sequencia de fibonnaci "
print " 2 - Uma posicao da sequencia de fibonnaci "

opcao = input("opcao: ")

if opcao == 1:
	qtd_sequencia = input("Quantidade de numeros da sequencia: ") 
	for x in range(0, qtd_sequencia):
		print fib1
		fib3 = fib1+fib2
		fib1 = fib2
		fib2 = fib3

if opcao ==2:
	posicao = input("Posicao: ")
	for x in range(1, posicao):
		fib3 = fib1+fib2
		fib1 = fib2
		fib2 = fib3
	print fib1


	