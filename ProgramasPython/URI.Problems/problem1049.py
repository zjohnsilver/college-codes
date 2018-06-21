## 
## Animal
## URI ONLINE - Problema 1049 - Iniciante
##
## Created by Jon on 16.03.2016
##	

# -*- coding: utf-8 -*-

string1 = raw_input()
string2 = raw_input()
string3 = raw_input()

if string1 == "vertebrado":
	if string2 == "ave":
		if string3 == "carnivoro":
			print ("aguia")
			
		elif string3 == "onivoro":
			print ("pomba")
	
	elif string2 == "mamifero":
		if string3 == "onivoro":
			print ("homem")
			
		elif string3 == "herbivoro":
			print ("vaca")
			
elif string1 == "invertebrado":
	if string2 == "inseto":
		if string3 == "hematofago":
			print ("pulga")
			
		elif string3 == "herbivoro":
			print ("lagarta")
	
	elif string2 == "anelideo":
		if string3 == "hematofago":
			print ("sanguessuga")
			
		elif string3 == "onivoro":
			print ("minhoca")