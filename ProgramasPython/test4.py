valor = float(input())
cont = 0
print ("NOTAS:")
while valor>=100:
    valor = valor-100
    cont+=1
print ("%i nota(s) de R$ 100.00"%(cont))
valor = round(valor,2)
cont = 0
while valor>=50:
    valor = valor-50
    cont+=1
print ("%i nota(s) de R$ 50.00"%(cont))
valor = round(valor,2)
cont = 0
while valor>=20:
    valor = valor-20
    cont+=1
print ("%i nota(s) de R$ 20.00"%(cont))
valor = round(valor,2)
cont = 0
while valor>=10:
    valor = valor-10.00
    cont+=1
print ("%i nota(s) de R$ 10.00"%(cont))
valor = round(valor,2)
cont = 0
while valor>=5:
    valor = valor-5
    cont+=1
print ("%i nota(s) de R$ 5.00"%(cont))
valor = round(valor,2)
cont = 0
while valor>=2:
    valor = valor-2
    cont+=1
print ("%i nota(s) de R$ 2.00"%(cont))
valor = round(valor,2)
cont = 0
print ("MOEDAS:")
while valor>=1:
	valor = valor -1
	cont+=1
print ("%i moeda(s) de R$ 1.00"%(cont))
valor = round(valor,2)
cont = 0
while valor>=0.5:
    valor = valor - 0.5
    cont+=1
print ("%i moeda(s) de R$ 0.50"%(cont))
valor = round(valor,2)
cont = 0
while valor>=0.25:
    valor = valor - 0.25
    cont+=1

print ("%i moeda(s) de R$ 0.25"%(cont))
valor = round(valor,2)
cont = 0
while valor>=0.10:
    valor = valor - 0.10
    cont+=1
print ("%i moeda(s) de R$ 0.10"%(cont))
valor = round(valor,2)
cont = 0
while valor>=0.05:
    valor = valor - 0.05
    cont+=1
print ("%i moeda(s) de R$ 0.05"%(cont))
valor = round(valor,2)
cont = 0

while valor>=0.01:
	valor = valor - 0.01
	valor = round(valor,2)
	cont+=1
print ("%i moeda(s) de R$ 0.01"%(cont))