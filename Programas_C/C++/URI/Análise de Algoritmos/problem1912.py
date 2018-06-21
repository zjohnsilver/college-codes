PRECISAO = 0.00001

def main():
	entrada = raw_input().split()
	entrada = [int(x) for x in entrada]
	
	
	while (entrada[0] or entrada[1]):
		alturas = raw_input().split()
		alturas = [int(x) for x in alturas]
		
		if (abs(sum(alturas) - entrada[1]) < PRECISAO):
			print ":D"		
		else: 
			if (sum(alturas) < entrada[1]):
				print "-.-"
			else:			
				retorno = (busca_Binaria(entrada, alturas, 0, max(alturas)))
				print "%.4f" %(retorno)
			
		entrada = raw_input().split() 
		entrada = [int(x) for x in entrada]
		


def busca_Binaria(entrada, alturas, menor, maior):
	meio = (menor+maior)/2.0

	soma = 0
	
	for x in alturas:
		if (x - meio) > 0:
			soma += (x-meio)

	if (abs(soma - entrada[1]) < PRECISAO):
		return meio
	else:
		if (soma < entrada[1]):
			return busca_Binaria(entrada, alturas, menor, meio)
		else:
			return busca_Binaria(entrada, alturas, meio, maior)
    
main()
