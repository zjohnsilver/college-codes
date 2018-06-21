# Controle de cotas de disco #

arquivo = open("usuarios.txt", "r")
string = arquivo.read()
arquivo.close()

def convert_MB (valor_KB):
	return valor_KB/(1024**2)

def percentual_uso (valor, soma):
	return (valor/soma)*100


def main():
	#Posicões pares estão os nomes
	#Posições impáres estão os consumos
	dados = string.split() #Lista com os dados

	#Calculo do total de espaço ocupado e converção em MB
	soma = 0
	for x in range(1, len(dados), 2):
		dados[x] = convert_MB(int(dados[x]))
		soma += dados[x]
		dados[x] = "%.2f"%(dados[x]) #Armazenando valores com precisão de 2 casas decimais

	arquivo = open("relatório.txt", "w")

	arquivo.write("ACME Inc.           Uso do espaço em disco pelos usuários\n")
	arquivo.write("------------------------------------------------------------------------\n")
	arquivo.write("Nr.  Usuário        Espaço utilizado     % do uso\n\n\n")

	y = 1
	for x in range(0, (len(dados)), 2):
		arquivo.write("%-5d%-15s%7s%3s%17.2f%%\n" %(y, dados[x], dados[x+1], "MB", percentual_uso(float(dados[x+1]), soma)))
		y+=1

	arquivo.write("\n\nEspaço total ocupado: %.2f MB"%(soma))
	arquivo.write("\nEspaço médio ocupado: %.2f MB"%(soma/6))

	arquivo.close()

main()






