y = int(input("Número: "))

h = 1
print ("%i!"%(y), end = " = ")
for x in range(1,y+1):
	h = h * x
	if x!=y:
		print ("%i"%(x), end= " . ")
	else:
		print("%i"%(x), end = "")

	
print (" = %i"%(h))