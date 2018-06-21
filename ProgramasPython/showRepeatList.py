#!usr/bin/python
#coding=utf-8

#  Faça um programa que leia 10 valores e coloque em uma lista. Depois, mostre quais elementos da lista estão repetidos e quantas vezes cada um se repete.

lista = [ ]
listarepeat = [ ]
for x in range(10):
	lista.append(input("Número: "))

for j in range(10):
	z=1
	for i in range(10):
		if j!=i:
			if lista[j]==lista[i]:
				z+=1
				valor=lista[i]
	if z>1 and valor!=x:	
		print "O valor %i se repete %i vezes."%(valor,z)	
	x=valor

print listarepeat
	
		
