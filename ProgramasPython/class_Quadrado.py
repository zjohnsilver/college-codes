import random

class Quadrado:
	def __init__ (self, lado = 0):
		self.lado = lado

	def area (self):
		return ("Area: %.2f" %(self.lado*self.lado))

	def perimetro (self):
		return ("Perimetro: %.2f" %(self.lado*4))

	def diagonal (self):
		return ("Diagonal: %.2f" %(((self.lado)**2 +
								  (self.lado**2))**0.5))


def main():

	#Gerando dados para testar a classe
	for x in range(10):
		lado = random.randint(1,50)/50.0
		quadrado = Quadrado(lado)
		print (quadrado.lado)
		print (quadrado.area())
		print (quadrado.perimetro())
		print (quadrado.diagonal())

		print("\n")

main()
