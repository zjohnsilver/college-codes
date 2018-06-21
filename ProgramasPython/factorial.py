#!/usr/bin/python
#coding=utf-8

num=input("Número: ")
fat=1
fat2=str(num)+""
#Programa em For

for x in range(num,0,-1):
	fat=fat*x
	if num<fat:
		fat2=fat2+"."+str(x)

print "O fatorial do número %i é %i."%(num,fat)
print "Ou %i! = %s = %i"%(num,fat2,fat)

fat=1
aux=num
"""
#Programa em While

while num>0:
	fat=fat*num
	num-=1

print "O fatorial do número %i é %i."%(aux,fat)
print "Ou %i! = %i."%(aux,fat)



"""
#Lancelot
