"""
11) Faca um programa que recebe uma lista com modelos de 5 carros e outra com o consumo de
cada modelo. Mostre o modelo mais economico e quantos litros cada modelo gasta para percorrer
uma distancia de 1000 Km.
"""

modelos = [ ]

consumo = [ ]

for x in range(5):
	modelos.append(raw_input("Modelo: "))
	consumo.append(input("Consumo: "))
	

menor=consumo[0]

for x in range(1,5):
	if consumo[x]<menor:
		menor=consumo[x]
		modelo=modelos[x]
		
print "O carro com menor consumo e ",modelo,"."

for x in range(5):
	print "O modelo",modelos	[x],"consome em 1000 km: ",consumo[x]*1000,"litros."
	
	
#Lancelot
