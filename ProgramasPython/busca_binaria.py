#### BUSCA BINARIA ####



def main():
	vetor = [1,4,6,10,30,40,50,55, 64]

	inicio = 0
	fim = len(vetor)-1

	print ("Vetor: %s"%(vetor))

	buscar = input("Deseja buscar qual valor: ")

	while True:
		i = (len(vetor))//2
		fim = len(vetor) -1

		print (i, inicio, fim, vetor)
		if vetor[i] == buscar:
			print ("Voce encontrou")
			break

		if inicio == fim:
			print ("Nao encontrou o elemento procurado")
			break
		else:
			if vetor[i] < buscar:
				vetor = vetor[i+1:]
				inicio = i+1

			elif vetor[i] > buscar:
				vetor = vetor[:i]



main()
