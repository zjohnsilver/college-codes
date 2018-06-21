#!usr/bin/python
#coding=utf-8

# Faça um programa que recebe uma lista de quantidade de elementos definida pelo usuário. O programa deve mostrar o menor número da lista e as posições da lista em que esse valor aparece.

lista = [ ]
listapos = [ ]
qtd = input("Quantidade: ")

for x in range(qtd):
	lista.append(input("Número: "))
	if x==0:
		menor=lista[0]
	if lista[x]<menor:
		menor=lista[x]
for x in range(qtd):
	if menor==lista[x]:
		listapos.append(x)	

print "Menor valor: %i"%(menor)
print "Lista contendo as posições em que o menor valor aparece: %s."%(listapos)

#Lancelot
		

