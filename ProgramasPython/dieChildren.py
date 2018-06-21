#!usr/bin/python
#coding=utf-8

#ÍNDICE DE MORTALIDADE INFANTIL EM UM DETERMINADO PERÍODO

num=input("Qtd. Crianças: ")
contM=0
contF=0
contL=0
for x in range(num):
	sexo=raw_input("M-Masculino or F-Feminino: ")
	if sexo=="M":
		contM+=1
	if sexo== "F":
		contF+=1
	timelife=input("Tempo de Vida em Meses: ")
	if timelife<=24:
		contL+=1
print ""

print "PORCENTAGEM CRIANÇAS SEXO MASCULINO: %.2f%%." %(contM*100/num)

print "PORCENTAGEM CRIANÇAS SEXO FEMININO: %.2f%%." %(contF*100/num)

print "PORCENTAGEM CRIANÇAS QUE VIVERAM 24 MESES OU MENOS: %.2f%%." %(contL*100/num)
	

#Lancelot
