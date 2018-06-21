def fined(string, sub_string):
	for y in range(len(string)-(len(sub_string)-1)):   # 3 letras - (2 letras - 1) = 2 (0,1) 
		if string[y:y+(len(sub_string))] ==  sub_string:
			return True
	return False


print (fined("ola","la"))

# 
"""
OLHAR

FÓMULA: QTD_LETRAS - (QTD_AGRUPAMENTOS -1) (QUANTIDADES DE SEPARAÇÕES)

OLA
OL LA



string[0:2]      
string[1:3]


OLHA

OL LH HA

OLHAR

OL LH HA AR
"""