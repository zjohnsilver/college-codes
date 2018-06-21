##
## Pontos dentro de uma circunferencia de raio R
##
## Created by Jon on 11.03.2016
##

raioo = input("Raio: ")
raio = int(raioo)

x = -raio
y = -raio

qtd_pontos = 0 

while -raio<=x<=raio:
	y = -raio
	
	while -raio<=y<=raio:
	
		if (x**2 + y**2) <= raioo **2:
			print ("(%d,%d)"%(x,y))
			qtd_pontos+=1
			
		y+=1
	x+=1

print ("Total de pontos: %d"%(qtd_pontos))