## 
## Receber x,y e determinar o quadrante. Sobre o eixo: Eixo X, Eixo Y.
## Na origem: x=y=0: Imprimir:  Origem
## URI ONLINE - Problema 1041 - Iniciante
##
## Created by Jon on 07.03.2016
##

# -*- coding: utf-8 -*-

string = raw_input().split() ## Recebe dois valores

X = float(string[0])
Y = float(string[1])

## Condicoes para X=Y=0 ou somente X=0 ou somente Y=0
if X==Y==0:
    print ("Origem")
    
elif X==0:
    print ("Eixo Y")
    
elif Y==0:
    print ("Eixo X")
    
## Condicoes para saber a qual quadrante pertence
if X>0 and Y>0:
    print ("Q1") 
    
if X<0 and Y>0:
    print ("Q2")
    
if X<0 and Y<0:
    print ("Q3")
    
if X>0 and Y<0:
    print ("Q4")
