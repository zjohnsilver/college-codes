##
## Entrada é uma tecla danificada e o valor digitado
## Saída é o valor que vai ser impresso considerando a tecla danificada
##  
## URI ONLINE - Problema 1120 - Strings
##
## Created by Jon on 15.06.2016
##
## Python 3


caso_teste = []

while (caso_teste != ['0', '0']):
	caso_teste = input().split()
	saída = ''

	for num in caso_teste[1]:
		if num != caso_teste[0]:
			saída += num
	if saída == '':
		saída = '0'
	if (caso_teste != ['0', '0']):
		print (int(saída))