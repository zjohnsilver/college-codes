#!/usr/bin/python
#coding=utf-8

turma=1
maior=menor=0
while turma<=30:
	altura=input("Altura %i: "%(turma))
	if altura>maior:
		maior=altura
	if altura<menor or turma==1:
		menor=altura
	
	turma+=1
	

print "O maior mede %.2fm. E o menor mede %.2fm."%(maior,menor)

#Lancelot
