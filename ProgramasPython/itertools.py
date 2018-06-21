from itertools import *

from platform import python_version
print (python_version()) 


# GENERATOR
S = (x for x in count() if x**2 > 3)

## S e uma pilha, para andar em seus elementos: S.next(), este comando
## desempilha



#################################################

## COMPREENSAO DE LISTAS // NAO FAZ PARTE DO ITERTOOLS
S = [x*2 for x in range(101) if x ** 2 >= 1]


## Comando IZIP: Justa duas interacoes
## Ex:
first_name = "John"
#for i in izip(first_name, "-------",count(1)): #zipa varias "listas"
	#print str(i[0])+str(i[1])+str(i[2]) # Seu retorno sao tuplas
	

# ACCUMULATE
#nums = list(accumulate(range(8)))









