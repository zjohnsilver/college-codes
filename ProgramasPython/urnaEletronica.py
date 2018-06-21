##
## Urna Eletronica
##
## Created by Jon on 11.03.2016
##

chapa_1 = 0
chapa_2 = 0
chapa_3 = 0
branco = 0
nulo = 0
total = 0


for x in range(1,5):
	
	voto = input("Voto: ")
	confirmar = raw_input()
	if confirmar == 'N' or confirmar == 'n' or confirmar == "nao":
		while confirmar == 'N' or confirmar == 'n' or confirmar == "nao":
			voto = input("Voto: ")
			confirmar = raw_input()
	else:
		print ("Confirmado!! ")
	
	if voto == 1:
		chapa_1+=1
		
	elif voto == 2:
		chapa_2+=1
		
	elif voto == 3:
		chapa_3+=1
	
	elif voto == 0:
		branco+=1
	
	else:
		nulo+=1

	total+=1
	
		
print ("%% Votos Chapa_1: %.2f"%((float(chapa_1)/total)*100))

print ("%% Votos Chapa_2: %.2f"%((float(chapa_2)/total)*100))

print ("%% Votos Chapa_3: %.2f"%((float(chapa_3)/total)*100))

print ("%% Votos Brancos: %.2f"%((float(branco)/total)*100))

print ("%% Votos Nulos: %.2f"%((float(nulo)/total)*100))

if chapa_1 > (50.0/100)*total:
	print "Chapa 1 ganhou!!"

elif chapa_2 > (50.0/100)*total:
	print "Chapa 2 ganhou!!"

elif chapa_3 > (50.0/100)*total:
	print "Chapa 3 ganhou!!"
	
else:
	print "Segundo turno."
	
		
		
	
	
