#!usr/bin/python
#coding=utf-8 

# Faça um programa que recebe os elementos de duas listas de 10 posições. O programa deve mostrar a intercalação entre as listas.

listx = [ ]
listy = [ ]
listxy = [ ]

print"Lista X:\n"

for x in range(10):
	listx.append(input("Número list X: "))
print ""
print "Lista Y:\n"
for y in range(10):
	listy.append(input("Número list Y: "))


for i in range(10):
	listxy.append(listx[i])
	listxy.append(listy[i])

print "Lista X: %s e \nLista Y: %s \n"%(listx,listy)
print "Intercalação entre as listas X e Y: \n%s"%(listxy)

