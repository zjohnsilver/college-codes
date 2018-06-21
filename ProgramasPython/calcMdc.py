
# Calculando o MDC entre dois numeros

num1= input("Numero: ")
num2= input("Numero: ")

num4,num5=num1,num2


test = True

if num1<num2:
	aux=num1
	num1 = num2
	num2 = aux

while test == True:
	num3=num1%num2
	if num3 != 0:
		num1=num2
		num2=num3
	if num3 == 0:
		test=False
		print ""
		if num2!=1:
			print "MDC(%i,%i)"%(num4,num5) + " = %i"%(num2)
		if num2==1:
			print "MDC(%i,%i)"%(num4,num5) + " = %i"%(num2)
			print "Sao primos entre si."
			
def mdc(x,y):  # FUNCAO MDC
	num4,num5=x,y
	if x<y:
		aux=x
		x =  y
		y = aux
	test=True
	while test == True:
		num3=x%y
		if num3 != 0:
			x=y
			y=num3
		if num3 == 0:
			test=False
			print ""
			if num2!=1:
				return "MDC(%i,%i)"%(num4,num5) + " = %i"%(y)
			if num2==1:
				print "MDC(%i,%i)"%(num4,num5) + " = %i"%(y)
				print "Sao primos entre si."
				return ""
print mdc(7,12), mdc(7,17),mdc(12,17)


		
		