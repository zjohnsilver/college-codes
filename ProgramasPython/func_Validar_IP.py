#Função validar IP: Nenhum dos 4 números pode ser maior que 255, pois 8 bits só armazenam até 255#

import random


def validar_IP (endereco_IP):
	nums_IP = endereco_IP.split('.')

	for num in nums_IP:
		if int(num)>255:
			return False

	return True


cont_Valid = cont_Invalid = 0


## Testando a funcao ##
for qtd in range(10000000):
	IP = []
	for num in range(4):
		number = random.randint(0.500)
		IP.append(str(number))

	IP = '.'.join(IP)

	if validar_IP(IP):
		cont_Valid += 1

	else:
		cont_Invalid += 1


# Imprimindo qtd de endereços válidos e inválidos
print ("Válidos: %d\nInválidos: %d" %(cont_Valid, cont_Invalid))