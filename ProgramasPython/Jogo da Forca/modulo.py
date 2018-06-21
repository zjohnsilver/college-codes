import random

def ler_arquivo():
    dicas_palavras = {}
    arquivo = open("palavras", "r")
    for linha in arquivo.readlines():
        if linha[0] == '#':
            dica = linha.split('#')[1].upper()
            dicas_palavras[dica] = [] ## Pegando a dica e criando uma lista das palavras daquela dica.
        else:
            dicas_palavras[dica].append(linha[:len(linha)-1].upper()) ##Removendo o '\n'
	
    arquivo.close()
    return dicas_palavras
    
dicas_palavras = ler_arquivo()

        
def sorteio_dica():
    global dicas_palavras
    dica = random.choice(list(dicas_palavras.keys()))  ## Sorteando a dica
    return dica

  
## Encontra os indices que devem ser mudados na palavra
def busca_indices (palavra, chute):  
	indices = []
	for index, letra in enumerate(palavra):
		if chute == letra:
			indices.append(index)
			
	return indices
	
def modifica_word (word, indices, chute):
	for index in indices:
		word[index] = chute
	return word
	 
etapa = {
'1': 
"""
 *****
 *   *
 *
 *
 *
 *
 *
 *
*****
	""",
'2': 	
"""
 *****
 *   *
 *   |
 *  
 *
 *
 *
 *
*****
	""",
'3':
"""
 *****
 *   *
 *   |
 *  /
 *
 *
 *
 *
*****
	""",
'4':
"""
 *****
 *   *
 *   |
 *  / \\
 *
 *
 *
 *
*****
	""",
'5':
"""
 *****
 *   *
 *   |
 *  /|\\
 *   |
 *
 *
 *
*****
	""",
'6':
"""
 *****
 *   *
 *   |
 *  /|\\
 *   |
 *  /
 *
 *
*****
	""",
'7':
"""
 *****
 *   *
 *   |
 *  /|\\
 *   |
 *  / \\
 *
 *
*****
	"""}