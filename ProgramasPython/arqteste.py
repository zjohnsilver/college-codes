
def test():
	arquivo = open("teste.txt","a")
	x=int(input("Digite: "))
	arquivo.write(str(x))
	arquivo.close()


	arquivo = open("teste.txt","r")

	ler = arquivo.read()

	arquivo.close()

	print (ler)