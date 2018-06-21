#!/usr/bin/python
#coding=utf-8

qtd=input("Quantidade de Valores: ")
fat=1
for x in range(1,qtd+1):
	num=input("Número %i: "%(x))
	aux=num
	while num>0:
		fat=fat*num
		num-=1
	print "%i! = %i."%(aux,fat)
	fat=1


#Lancelot
	
