#!usr/bin/python
#coding=utf-8

import random

testes=int(input("Número de testes: "))

trocar = 0
n_trocar=0
for i in range(testes):
	porta = random.randrange(1,4)
	premio = random.randint(1,3)
	
	if porta==premio:
		trocar += 1
	else:
		n_trocar += 1

print "É vantajoso trocar em %.3g %% das vezes"%(trocar*100/testes)

print "Não é vantajoso trocar em %.3g %% das vezes"%(n_trocar*100/testes)



