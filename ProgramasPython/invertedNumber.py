#!usr/bin/python
#coding=utf-8

num=input("Número: ")
invertido=""
while num>0:
	num1=num%10
	num=num//10
	invertido=invertido+str(num1)
print invertido
	
#Lancelot
