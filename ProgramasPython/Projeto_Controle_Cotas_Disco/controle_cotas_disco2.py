# Controle de cotas de disco #

arquivo = open("usuarios.txt", "r")
login_espaco = arquivo.read()
arquivo.close()

def convert_MB (valor_KB):
	return valor_KB/(1024**2)

def percentual_uso (valor, soma):
	return (valor/soma)*100


def main():
	#Posicões pares estão os nomes
	#Posições impáres estão os consumos
	lista_dados = login_espaco.split() #Lista com os dados
	dados = {}

	#Calculo do total de espaço ocupado e converção em MB
	soma = 0
	for x in range(0, len(lista_dados), 2):
		dados[lista_dados[x]] = "%.2f" %(convert_MB(int(lista_dados[x+1])))
		soma+= float(dados[lista_dados[x]])


	arquivo = open("relatório.txt", "w")

	arquivo.write("ACME Inc.           Uso do espaço em disco pelos usuários\n")
	arquivo.write("------------------------------------------------------------------------\n")
	arquivo.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n\n")

	y = 1
	for nome in dados.keys():
		arquivo.write("%-5d%-15s%7s%3s%17.2f%%\n" %(y, nome, float(dados[nome]), "MB", percentual_uso(float(dados[nome]), soma)))
		y+=1

	arquivo.write("\n\nEspaço total ocupado: %.2f MB"%(soma))
	arquivo.write("\nEspaço médio ocupado: %.2f MB"%(soma/6))

	arquivo.close()

main()






