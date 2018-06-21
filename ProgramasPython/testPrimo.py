#!usr/bin/python
#coding=utf-8

num=input("Número: ")
div=0
test=True
print""
while test:
	if num>=1:
		for x in range(1,num+1):
			if num%x==0:
				div+=1
		test=False
		if div==2:
			print "NÚMERO %i É PRIMO."%(num)
		else:
			print "NÚMERO %i NÃO É PRIMO."%(num)

	else:
		while num<1:
			num=input("Número: ")


#Lancelot


