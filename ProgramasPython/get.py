dic = {"Nome":"John", "Telefone":97235246}


def get(dicionario, chave, valor =  None):
	if chave in dicionario:
		return dicionario[chave]
	else:
		return valor
	
print (get(dic,"Nome"))
	