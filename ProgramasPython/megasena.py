# MEGASENA

import random

meu = [1,4,14,16,20,47]

megasena = list(range(1,61))

sorteado = [ ]

n = int(input("Número de tentativas: "))


for x in range(1,n):
	sorteado = []
	
	cont = 0


	
	while meu !=sorteado:
		mega_sorte=megasena.copy()
		sorteado = []
		for i in range(6):
			num_sorteado = random.choice(mega_sorte)
			sorteado.append(num_sorteado)
			mega_sorte.remove(num_sorteado)
			
			
		sorteado.sort()
		
		
		cont +=1
		
	soma+=cont
		
	print ("Resultado do teste %i: %i tentativas"%((x+1),cont))

soma /=n

print ("Média dos resultados: ", soma)
