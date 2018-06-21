# Encontrando os elementos invertíveis de um conjunto Módulo n #


modulo =  int(input("Módulo: "))

inversos = [ ]

def mdc(num1,num2):
	if num1 >num2:
		aux = num1
		num1 = num2
		num2 = aux
	max=0
	for x in range(1,num1+1):
		if num1%x==0 and num2%x==0:
			max=x
	return max

def primo(n):
	cont = 0
	for x in range(1,n+1):
		if n % x == 0:
			cont +=1
	if cont ==2:
		return True
	return False
	

for x in range(1,modulo):
	b = mdc(x,modulo)
	if b ==1:
		inversos.append(x)
		
		
print ("Inversos do Módulo %i: %s"%(modulo,inversos))

# Calculando @(n) do conjunto (Calculando PHI, ou Euler, não tinha o símbolo para usar =P)


phi = int(input("Digite o Valor de PHI ou Euler: "))

if primo(phi) == True:
	print ("Phi vale: %i"%(phi-1))
else:
	print ("Ou é PAR ou é um Primo elevado a um potência. ")

