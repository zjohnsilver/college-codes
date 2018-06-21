from profundidade_limitada import *

def aprof_iterativo(est_inicial, objetivo):
	resposta = None
	sucesso = False
	limite = 1
	while (not sucesso):
		resposta = sucesso = busca_profund_limitada(est_inicial, objetivo, limite)
		
		print limite, sucesso
		
		if sucesso == False:
			limite+=1
	return resposta
	

inicio = raw_input("Inicio: ")
final = raw_input("Final: ")	
	
print aprof_iterativo(inicio, final)
