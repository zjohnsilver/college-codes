#!usr/bin/python
#coding=utf-8
num1=input("Número I: ")
num2=input("Número II: ")
max=0
for x in range(1,num1+1):
	if num1%x==0 and num2%x==0:
		max=x
print ""
if max==1:
	print "Os números %i e %i são primos entre si."%(num1,num2)
else:
	print "O mdc entre %i e %i é %i."%(num1,num2,max)
		

#Lancelot

		
