## 
## Tipos de Triangulo
## URI ONLINE - Problema 1045 - Iniciante
##
## Created by Jon on 16.03.2016
##	

# -*- coding: utf-8 -*-

string = raw_input().split()

A = float(string[0])
B = float(string[1])
C = float(string[2])

## Ordenando em ordem decrescente
if A<B:
	aux = A
	A = B
	B = aux
if A<C:
	aux = A
	A = C
	C = aux

if B<C:
	aux = B
	B = C
	C = aux

	
## Condicoes da questao	
if A>=B+C:
	print ("NAO FORMA TRIANGULO")
	
else:
	
	if A**2 == B**2 + C**2:
		print ("TRIANGULO RETANGULO")
		
	elif A**2 > (B**2 + C**2):
		print ("TRIANGULO OBTUSANGULO")
		
	elif A**2 < (B**2 + C**2):
		print ("TRIANGULO ACUTANGULO")

	if A==B==C:
		print ("TRIANGULO EQUILATERO")

	elif A==B or A==C or B==C:
		print ("TRIANGULO ISOSCELES")	
