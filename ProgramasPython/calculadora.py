#!usr/bin/python
#coding=utf-8

print "---------------------------------------------------------------------------"
print "                             CALCULADORA                                   "
print "---------------------------------------------------------------------------"
x=True
resultado=input("Valor:")
while x==True:
	
	operacao= raw_input("Operação:")
	if operacao != "":
		recebe=input("Valor:")
	

	if operacao == "+":
		resultado = resultado + recebe

	if operacao == "-":
		resultado = resultado - recebe

	if operacao == "x":
		resultado = resultado * recebe
	
	if operacao == "":
		x=False

print "\n"
print "Resultado: %.2f" %(resultado)
	 
