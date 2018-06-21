#!/usr/bin/python
#coding=utf-8
x=input("Quantidade de primos: ")
div=0
qtd=0
num3=2
while qtd<x:
	for i in range(1,num3+1):
		if num3%i==0:
			div=div+1
	if div==2:
		print num3
		qtd=qtd+1
	div=0
	num3=num3+1
	
	

#Lancelot
