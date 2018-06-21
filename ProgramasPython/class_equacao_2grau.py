import random

class segundo_grau:
	def __init__ (self, a = 1, b = 2, c = 1):
		self.a = a
		self.b = b
		self.c = c
		self.delt = 0

	def delta (self):
		self.delt = (self.b**2 - 4*self.a*self.c)
		return self.delt

	def raizes (self):
		if self.delt >= 0:
			raiz1 = ("%.2f")%((-self.b + (self.delt**0.5))/(2.0*self.a))
			raiz2 = ("%.2f")%((-self.b - (self.delt**0.5))/(2.0*self.a))
			return ((float(raiz1), float(raiz2)))
		else:
			return "Delta Negativo, impossível cálcular raízes."



def main():
	cont_pos = cont_neg = 0
	for x in range(1000):
		a = 0
		b = 0
		c = 0

		while a == 0 or b ==0 or c==0:
			a = random.randint(-10, 10)
			b = random.randint(-10, 10)
			c = random.randint(-10, 10)

		funcao = segundo_grau(a, b, c)

		print ("Delta: %d"%(funcao.delta()))

		if funcao.delt>=0:
			print ("""Raízes: %f e %f""" %(funcao.raizes()[0], funcao.raizes()[1]))
			cont_pos += 1

		else:
			print (funcao.raizes())
			cont_neg += 1

		print ("\n")

	#Quantas combinações deram deltas positivos e quantas deram delta negativo
	#Ou quantas conseguiram calcular as raízes e quantas não	
	print ("Positivos: %d\nNegativos: %d"%(cont_pos, cont_neg))


main()

