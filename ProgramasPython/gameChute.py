import random

number = random.randint(1,100)


def main():
	print ("Adivinhe qual número estou pensando...")
	cont_Chutes = 0
	while True:
		chute = int(input("Chute: "))
		cont_Chutes+=1
		if chute == number:
			print ("\nParabéns! Você acertou o número que eu estava pensando..")
			print ("\nPara isso você precisou de %i chutes."%(cont_Chutes))
			break
		if chute>number:
			print("\nTente chutar um número mais baixo..")
		if chute<number:
			print("\nTente chutar um número mais alto..")
			
			
main()
			