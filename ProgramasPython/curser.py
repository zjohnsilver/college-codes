
	### Substitui uma string de entrada, por asteriscos, baseado em um outro argumento da funcao ###
	### "Hey Hey Hey", "Hey": Deve retornar *** *** ***, ja que o parametro usado foi a palavra "Hey"

def censor (text, word):
    lista = text.split()
    
    for index, palavra in enumerate(lista):
        if word == palavra:
            lista[index] = '*' * len(word)
            
    return " ".join(lista)



print censor ("Hey Hey Hey", "Hey")