#!/usr/bin/python
#coding=utf-8

number=input("Number one: ")
number2=input("Number two: ")
digit=0
result=number*number2

aux = result

while aux != 0:

	aux=aux//10
	digit +=1

print "O resultado da múltiplicação é %.i, e esse número tem %.i dígitos."%(result, digit)

#Lancelot
