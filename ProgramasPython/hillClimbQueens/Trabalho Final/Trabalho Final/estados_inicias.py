from trabalhoFinally import *

arquivo = open("estados_inicias.txt", "w")


for x in range(5):
	resp = gerarInicio()

	inicio = resp[0]

	arquivo.write(str(inicio.caminho))
	arquivo.write("\n")
	arquivo.write(str(inicio.custo))



arquivo.close()



