#!usr/bin/python
#coding=utf-8

# Escreva um programa que receba uma lista de quantidade de elementos digitada pela usuário e depois recebe um outro valor. O programa deve mostrar na tela "ACHADO" se o valor estiver na lista e "NÃO ACHADO" caso contrário.

lista = [ ]
qtd = input("Número de Elementos: ")
y=""

for x in range(qtd):
	lista.append(input("Número: "))

valor = input("Valor: ")

for x in range(qtd):
	if valor==lista[x]:
		y=lista[x]

print ""
if y=="":
	print "NÃO ACHADO"
else:
	print "ACHADO"

#Lancelot



