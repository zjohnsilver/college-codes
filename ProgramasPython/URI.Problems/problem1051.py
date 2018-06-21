## 
## Imposto de Renda
## URI ONLINE - Problema 1051 - Iniciante
##
## Created by Jon on 16.03.2016
##	

# -*- coding: utf-8 -*-

salario = input()

total = 0

if 0.00<salario<=2000.00:
	print ("Isento")

else:
	if 2000.00<salario<=3000.00:
		total = (salario-2000) *0.08
		
	if 3000.00<salario<=4500.00:
		total = ((salario-3000)*0.18) + 80.00 ## Esse 80 e o acumulado da diferenca do if anterior vezes 0.08
		
	if salario > 4500.00:
		total = ((salario-4500)*0.28) + 350.00 ## Esse 350 e o acumulado da diferenca do if anterior vezes 0.18 + 80(acumulado da diferenca do primeiro if vezes 0.08)
	
	print ("R$ %.2f" %(total))