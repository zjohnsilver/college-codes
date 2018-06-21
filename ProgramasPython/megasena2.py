# MEGASENA, mas com um jogo teorico.

import random


megasena = list(range(1,61))

sorteado = [ ]

n = int(input("Número de tentativas: "))


for x in range(1,n):
	sorteado = []
	meu = []
	cont = 0
	mega_sorte=megasena.copy()
	for j in range(6):
		num_sorteado = random.choice(mega_sorte)
		meu.append(num_sorteado)
		mega_sorte.remove(num_sorteado)
	meu.sort()
	
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
	print ("Jogo que ganhou:",meu)	
	print ("Resultado do teste %i: %i tentativas"%((x+1),cont))

soma /=n

print ("Média dos resultados: ", soma)
