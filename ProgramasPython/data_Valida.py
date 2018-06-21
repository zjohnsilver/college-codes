
"""
test = True
if (test):
	i = 0
	cont= 0
	dat = raw_input("Data:\n>>> ")
	data = dat.split('/')
	
	search_Barra = dat+ "."
	
	while (search_Barra[i] != '.'):
		if (search_Barra[i] == '/'):
			cont+=1
		i+=1
		
	if (cont==2):
		if (int(data[0])>31 | int(data[0])<1):
			test = False
			
		else:
			if (int(data[1])>12 | int(data[2])<1):
				test = False
			
			else:
				if (int(data[2])<1900):
					test = False			
	else:
		test = False

if (test==False):
	print ("Data Invalida.")
	
else:
	print ("Data Valida")
	
"""

date = raw_input("Data:\n>>> ")	

def data_Valida(dat): ## Funcao verifica se 1<=dia<=31, 1<= mes <= 12, ano>=1900
	i = 0
	cont= 0

	data = dat.split('/')
	
	search_Barra = dat+ "."
	
	while (search_Barra[i] != '.'):
		if (search_Barra[i] == '/'):
			cont+=1
		i+=1
		
	if (cont==2):
		if (int(data[0])>31 | int(data[0])<1):
			return "Data Invalida"
			
		else:
			if (int(data[1])>12 | int(data[2])<1):
				return "Data Invalida"
			
			else:
				if (int(data[2])<1900):
					return "Data Invalida"
					
	else:
		return "Data Invalida"
		
	return "Data Valida"
		
print ("%s" %(data_Valida(date)))