#!/usr/bin/python
# coding=utf-8

salario = 1000
anoatual = int(input("Ano: "))
aux = anoatual
mult = 1


while anoatual > 2005:
    salario2 = salario * (mult * 0.015) + salario
    anoatual -= 1
    mult = mult * 2


print("O salário desse funcionário em %i é de R$ %.2f." % (aux, salario2))

# Lancelot
