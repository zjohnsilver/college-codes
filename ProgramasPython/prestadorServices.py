"""
Uma empresa prestadora se serviços armazena informações sobre os serviços prestados. A empresa só pode atender até 3 cliente em cada dia. 
É de interesse da direção manter um histórico mensal sobre os serviços prestados.A empresa realiza 4 tipos de serviço: 1 – Pintura, 2 – Jardinagem, 3 – Faxina, 4 – Reforma em geral.
Cada serviço desenvolvido deve ser cadastrado com as seguintes informações: número do serviço, valor do serviço, código do serviço e código do cliente.
"""

def invalidCaracter(z):
	try:
		x = float(input("%s:"%(z)))
		return int(x)
	except:
		print ("Você digitou um caractere inválido.")
		return invalidCaracter(z)
		

print (" 1. Cadastrar tipos de serviço\
        \n 2. Cadastrar serviços prestados\
        \n 3. Mostrar os serviços prestados em um determinado dia\
        \n 4. Mostrar os serviços prestados em um intervalo de dias\
        \n 5. Mostrar um relatório geral (separado por dia), que exibe também a descrição do tipo de serviço.\
        \n 6. Sair")

n = invalidCaracter("Opção")

cadastros = []
cont = 0
if n==1:
	cadastros.append({})
	cadastros[cont]["num_Serviço"] = invalidCaracter("Número do Serviço")
	while cadastros[cont]["num_Serviço"]>4 or cadastros[cont]["num_Serviço"]<1:
		print ("Por favor, digite um um valor correspondente ao menu.")
		cadastros[cont]["num_Serviço"] = invalidCaracter("Número do Serviço")
	cadastros[cont]["valor_Serviço"] = invalidCaracter("Valor do Serviçoo")
	cadastros[cont]["codigo_Cliente"] = invalidCaracter("Código do Cliente")


	

	
	

	

		
