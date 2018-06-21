#!/usr/bin/python
#coding=utf-8

fib1=0
fib2=1
qtd=input("Número: ")
aux=qtd
vazio="1"

test=1

while test==1:
	while qtd>1:
		fib3=fib1+fib2
		vazio=vazio+" "+str(fib3)
		fib1=fib2
		fib2=fib3
		qtd-=1
	
	print "Sequência de Fibonacci com %i termos: %s"%(aux,vazio)
	test=input("Digite 1 para continuar e 2 para parar: ")
	if test==1:
		qtd=input("Número: ")


#Lancelot
