#!usr/bin/python
#coding=utf-8

print "----------------------------- PROGRAMA DAS 3 PORTAS-------------------------------------"

import random

print "Olá, Bem Vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!"

porta = input("Escolha uma porta: ")


print "Você escolheu a porta %.i, mas eu lhe informo que na porta %.i há um bode."%(porta,random.randint(1,3))

escolha = input("Deseja trocar de porta (1-Sim, 0-Não): ")

if escolha==1:
	porta = input("Escolha outra porta: ")
	x=random.randint(1,3)
	if x==porta:
		print "Parabéns você ganhou um carro!"
	else:
		print "Você escolheu a porta %.i. Que pena! Você ganhou um bode!"%(porta)
else:
	x=random.randint(1,3)
	if x==porta:
		print "Parabéns você ganhou um carro!"
	else:
		print "Que pena! Você ganhou um bode!"



