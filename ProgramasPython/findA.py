# Ache um elemento de a em Z34, de modo que todo elemento invertível de Z34 é um potência de a


for x in range(1,8,2):
	b = [ ]
	for y in range(1,8,2):
		z = (x**y) % 8
		b.append(z)
	if len(b) >=4:
		print ("Classe %i é %s"%(x,b))