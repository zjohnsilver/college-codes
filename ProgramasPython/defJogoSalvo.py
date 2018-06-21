def pos(z,x): # 1 - Inicio do For, 2 String a ser percorrida
	if z==0:
		for i in range(z,len(x)):
			if x[i] == ";":
				return i
	else:
		for i in range(pos(z-1,x)+1,len(x)):
			if x[i] == ";":
				return i

def jogoSalvo():
	arquivo = open("gameVelha.txt","r")
	ler = arquivo.readline()
	linha = ler[0:pos(0,ler)]
	coluna = ler[pos(0,ler)+1:pos(1,ler)]
	jogada = ler[pos(1,ler)+1:pos(2,ler)]
	return linha,coluna,jogada
	
print (jogoSalvo())