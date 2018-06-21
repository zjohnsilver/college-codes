#!usr/bin/python
#coding=utf-8

city=1
soma=0
maior=menor=0
citypert=0
citypert2=0
soma2=0
while city<=5:
	cidade=raw_input("Cidade: ")
	print cidade, "Informações: "
	veic=input("Veículos: ")
	acidentes=input("Acidentes: ")
	if acidentes>maior:
		maior=acidentes
		citypert=city
	if acidentes<menor or city==1:
		menor=acidentes
		citypert2=city
	soma=soma+veic
	if veic<2000:
		soma2=soma2+acidentes
	city+=1


print "Maior número de acidentes: %i, cidade %i. Menor número de acidentes: %i, cidade %i."%(maior,citypert,menor,citypert2)
print "Média de veículos: %i"%(soma/5)

print "Média de acidentes nas cidades com menos de 2000 veículos: %i/por cidade"%(soma2/5)


#Lancelot




