############################################
## Tipo de Combustivel
## URI ONLINE - Problema 1134 - Iniciante
##
## Created by Jon on 24.03.2016
##	

# -*- coding: utf-8 -*-


valor = 0 #Condicao do while

alcool = 0
gasolina = 0
diesel = 0

while valor!=4:
	valor = input() #Valor para teste
	
	while valor>4 or valor<1: #Pedir valor enquanto valor nao estiver na faixa de 1 a 4
		valor = input()	
	
	#Incrementando variaveis de contagem (alcool, gasolina, diesel)
	if valor == 1:
		alcool += 1

	elif valor == 2:
		gasolina += 1

	elif valor == 3:
		diesel += 1

#Saida do Programa
print ("MUITO OBRIGADO")
print ("Alcool: %d" %(alcool))
print ("Gasolina: %d" %(gasolina))
print ("Diesel: %d" %(diesel))

	
		
		
