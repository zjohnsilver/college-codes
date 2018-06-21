#!usr/bin/python
#coding=utf-8

print "-------------------------------------------------------------------------------------------------"
print "Área do Círculo, usando Módulo MATH."

raio=input("Raio: ")

from math import pi

area=pi*(raio**2)

from math import pow

area2=pi*pow(raio,2)
print ""
print "Area apenas com import pi: %.2f"%(area)
print "Area com import pi e pow: %.2f"%(area2)


#Lancelot
