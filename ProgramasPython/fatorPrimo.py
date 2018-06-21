##
## Fatores primos de um numero N
##
## Created by Jon in 21.03.2016
##

# -*- coding: utf-8 -*-

N = input()

y=2

print ("\nFatores Primos:\n")

while y<=N and N!=1:
	if N%y==0:
		print ("%d"%(y))
			
	while N%y==0:
		N = N/y	
		
	y+=1
			
