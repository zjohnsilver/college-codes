#!/usr/bin/python
#coding=utf-8

n=int(input("Valor N: "))
fat=1
E=1
for i in range(n,0,-1):
	for x in range(i,0,-1):
		fat=fat*x
	E=E+1/float(fat)
	fat=1
print ""
print "O valor da soma 1+1/1!+1/2!+..+1/%i! é %.10f."%(n,E)
	


#Lancelot
