def print_palavra(S, P, n):
	if (P[n] == 1):
		print (S[P[n]:n+1]),
	else:
		print_palavra(S, P, P[n]-1)
		print (S[P[n]:n+1]),	

palValidas = ["eu", "amo", "programar","e", "programa","a", "professor", "professora", "se", "garante","ensinando","ensina", "bem"]

S = " aprofessoraensinabem" #A string comeca com um caracter vazio, pois o algoritmo considera que a palavra comeca de 1.
#a string e contada de 1 a n
#No python o laco vai ate um valor n men. 1
n = len(S)-1

# O vetor V indica que ate um determinado
# indice a string e valida.
V = [i for i in range(n+1)] # V = [0...n]

#O vetor P armazena o Index onde termina
#as palavras da string S
P = [0 for i in range(n+1)] # P = [1...n], ignore o index 0

V[0] = True

for k in range(1, n+1): # k varia entre [1,n]
	V[k] = False
	for j in range (1, k+1): # j varia entre [1, k]
		if (V[j-1] and (S[j:k+1] in palValidas)): #S[j...k]
			print S[j:k+1]
			V[k] = True 
			P[k] = j #o index k e onde ela termina, e j e onde ela comeca
                     
print "P = " + str(P)
print V
print "n = " + str(n)

if V[n] == False:
	print "Nao"
else:
	print_palavra(S, P, n)
		
