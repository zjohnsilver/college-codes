## 
## Se os dados formarem um triangulo, imprima o perimetro, se nao, a area do trapezio..
## URI ONLINE - Problema 1043 - Iniciante
##
## Created by Jon on 14.03.2016
##

# -*- coding: utf-8 -*-

string = raw_input().split()

A = float(string[0])
B = float(string[1])
C = float(string[2])

if (A+B>C and A-B<C) and (B+C>A and B-C<A) and (A+C>B and A-C<B):
	print ("Perimetro = %.1f"%(A+B+C)) ## Perimetro do Triangulo
else:
	print ("Area = %.1f"%((A+B)*C/2.0)) ## Area do Trapezio
	
	