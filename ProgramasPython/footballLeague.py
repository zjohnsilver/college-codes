#!usr/bin/python
#coding=utf-8
soma=somaalt=inf18=maior80=0
for time in range(1,6):
	print "%i° Time -"%(time)
	print ""
	for jogador in range(1,12):
		print "JOGADOR %i: "%(jogador)
		idade=input("Idade: ")
		peso=float(input("Peso: "))
		altura=float(input("Altura: "))
		if idade<18:
			inf18+=1
		soma+=idade
		somaalt+=altura
		if peso>80:
			maior80+=1
		print "\n"
	print "Média das idades de jogadores do %i Time: %i anos"%(time,soma/11)
	soma=0
	print ""
	
	

print "Jogadores com idade inferior a 18: %i"%(inf18)
print "Média das alturas dos jogadores de todo o campeonato: %.2f"%(somaalt/55)

print "Porcentagem de jogadores com mais de 80Kg: %i %%"%((maior80*100)/55)
	

#Lancelot
