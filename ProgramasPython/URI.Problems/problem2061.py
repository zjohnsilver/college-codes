############################################
## As Abas de Péricles
## URI ONLINE - Problema 2061 - Iniciante
##
## Created by Jon in 19.06.2016
##	
## Python 3

teste = input().split()
abas = int(teste[0])
qtd_acoes = int(teste[1])

for x in range(qtd_acoes):
	acao = input()
	if acao == 'fechou':
		abas +=1
	elif acao == 'clicou':
		abas -= 1


print (abas)




