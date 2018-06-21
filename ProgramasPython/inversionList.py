#!usr/bin/python
#coding=utf-8

#Crie um programa que receba uma lista de inteiros de 30 posições e depois gera uma outra lista com os elementos do primeiro mas com a sequência invertida.

lista=[]
inversionlist=[]
for i in range(30):
	lista.append(int(input("Número inteiro: ")))

for x in range(29,-1,-1):
	inversionlist.append(lista[x])

print "Lista: \n %s\n"%(lista)
print "Lista Invertida: \n %s"%(inversionlist)
	

#Lancelot
