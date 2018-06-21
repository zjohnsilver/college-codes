#!/usr/bin/python
#coding=utf-8

base=input("Base: ")
altura=input("Altura: ")

while base==0 or altura==0:
	print "Por favor digite um número maior que zero(0)."	
	if base==0:
		base=input("Base: ")
	else:
		altura=input("Altura: ")
		
print "A área desse triângulo é %i"%(base*altura)

#Lancelot
