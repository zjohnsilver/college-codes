############################################
## Crescimento Populacional
## URI ONLINE - Problema 1160 - Iniciante
##
## Created by Jon in 19.06.2016
##	


qtd_testes = int(input())

for x in range(qtd_testes):
	teste = input().split()
	anos = 0
	while int(teste[0]) <= int(teste[1]) and anos<=100:
		teste[0] = int(teste[0]) + int(int(teste[0]) * (float(teste[2])/100.0))
		teste[1] = int(teste[1]) + int(int(teste[1]) * (float(teste[3])/100.0))
		anos += 1

	if anos<=100:
		print ("%d anos." %(anos))
	else:
		print ("Mais de 1 seculo.")
