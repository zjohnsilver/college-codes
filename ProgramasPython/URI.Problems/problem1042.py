## 
## Leia 3 valores inteiros e ordene-os em ordem crescente
## URI ONLINE - Problema 1042 - Iniciante
##
## Created by Jon on 14.03.2016
##

# -*- coding: utf-8 -*-

string = raw_input().split()

A = int(string[0])
B = int(string[1])
C = int(string[2])

D=A
E=B
F=C

if A>B:
    aux = A
    A = B
    B = aux
    
if A>C:
    aux = A
    A = C
    C = aux
    
if B>C:
    aux = B
    B = C
    C = aux

print A
print B
print C
print ""
print D
print E
print F