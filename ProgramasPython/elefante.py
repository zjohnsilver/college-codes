# PROGRAMA DA MÚSICA DO ELEFANTE...


for x in range(1,11):
	if x ==1 :
		print ("1 elefante incomoda muita gente.")
	elif x % 2 !=0:
		print ("%i elefantes incomodam muita gente."%(x))
	elif x % 2 == 0:
		print ("%i elefantes "%(x)+ "incomodam, "*(x-1)+"incomodam " +"muito mais.")
		print ("\n")


for x in range(10,0,-1):
	if x ==1 :
		print ("1 elefante incomoda muito menos.")
	elif x % 2 ==0:
		print ("%i elefantes incomodam muita gente."%(x))
	elif x % 2 != 0:
		print ("%i elefantes "%(x)+ "incomodam, "*(x-1)+"incomodam " +"muito menos.")
		print ("\n")
		