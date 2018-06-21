from tabuleiro import Tabuleiro
from funcoes import *
from copy import deepcopy


def moverUmaRainha(tabuleiro):
    colisoes = calculaColisoes(tabuleiro.tabuleiro)
    melhorTabuleiro = tabuleiro
    for ql in range(0,8):
    	for qc in range(0,8):
    		if tabuleiro.tabuleiro[ql][qc] == "Q":
	    		for ml in range(0,8):
	    			for mc in range(0,8):
	    				if tabuleiro.tabuleiro[ml][mc] != "Q":
	    					tentativa = deepcopy(tabuleiro.tabuleiro)
	    					tentativa[ql][qc] = '_'
	    					tentativa[ml][mc] = "Q"
	    					colisoesTentativa = calculaColisoes(tentativa)

	    					if colisoesTentativa < colisoes:
	    						colisoes = colisoesTentativa
	    						melhorTabuleiro.tabuleiro = tentativa
    melhorTabuleiro.custo = colisoes

    return melhorTabuleiro


def hillClimb():
	tabuleiro = gerarTabuleiro()

	while (1):

		vizinho = Tabuleiro()
		vizinho.tabuleiro = deepcopy(tabuleiro.tabuleiro)
		moverUmaRainha(vizinho)

		if (vizinho.custo >= tabuleiro.custo):
			return tabuleiro
		tabuleiro = vizinho



TOTAL_EXECUCOES = int(input("\nTotal Execuções: "))
colisoes_exec = {}

i = 0
while (TOTAL_EXECUCOES>i):
	print ("\nExecução: %d" %(i))

	solucao = hillClimb()
	colisoes = solucao.custo

	print ("\tColisões: %d" %(colisoes))

	if (i==0):
		melhor_solucao = Tabuleiro()
		melhor_solucao.tabuleiro = deepcopy(solucao.tabuleiro)
		melhor_solucao.custo = colisoes

	elif colisoes < melhor_solucao.custo:
		melhor_solucao.tabuleiro = deepcopy(solucao.tabuleiro)
		melhor_solucao.custo = colisoes


	if (str(colisoes) in colisoes_exec):
		colisoes_exec[str(colisoes)] +=1
	else:
		colisoes_exec[str(colisoes)] = 1

	i+=1


print ("\n\nTabela de Colisoes\n")

for i in colisoes_exec.keys():
	print ("Colisoes de " + i + ": " + str((colisoes_exec[i]*100)/TOTAL_EXECUCOES) + "%")


print ("\n\nMELHOR SOLUÇÃO: \n")

printarTabuleiro(melhor_solucao.tabuleiro)

print ("Custo: %d" %(melhor_solucao.custo))


