#!/usr/bin/python
#coding=utf-8

n=input("Número N: ")
soma=2
aux=n
pares="0"
soma2=0
while n>1:
	soma2=soma2+soma
	pares=pares+", "+str(soma)
	soma=soma+2
	n-=1
print ""
print "A soma dos %i primeiros números pares (%s) é %i."%(aux,pares,soma2)	

#Lancelot
