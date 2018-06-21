############################################
## Experiencias
## URI ONLINE - Problema 1094 - Iniciante
##
## Created by Jon on 21.03.2016
##	

# -*- coding: utf-8 -*-

qtd = input()
total = 0
qtd_Coelhos = 0
qtd_Sapos = 0
qtd_Ratos = 0

for x in range(1, qtd+1):
	string = raw_input().split()
	
	if string[1] == 'C':
		qtd_Coelhos += int(string[0])
		total += int(string[0])
		
	elif string[1] == 'R':
		qtd_Ratos += int(string[0])
		total += int(string[0])
		
	elif string[1] == 'S':
		qtd_Sapos += int(string[0])
		total += int(string[0])
		
print ("Total: %d cobaias"%(total))
print ("Total de coelhos: %d"%(qtd_Coelhos))
print ("Total de ratos: %d"%(qtd_Ratos))
print ("Total de sapos: %d"%(qtd_Sapos))

print ("Percentual de coelhos: %.2f %%"%((qtd_Coelhos/float(total))*100))
print ("Percentual de ratos: %.2f %%"%((qtd_Ratos/float(total))*100))
print ("Percentual de sapos: %.2f %%"%((qtd_Sapos/float(total))*100))





	