#!/usr/bin/python
#coding=utf-8

num1=input("Número 1: ")
num2=input("Número 2: ")
if num1>num2:
	aux=num1
	num1=num2
	num2=aux
aux1=num1
x=True

while x:
	if num1%num2==0:
		x=False
		print "MMC entre %i e %i é %i."%(aux1,num2,num1)
		
	num1=num1+aux1

#Lancelot & Jota Bê
	

	


			
