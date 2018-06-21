def replace(string, old_string, new_string):
	while string.find(old_string) >= 0:
		x= string.find(old_string)
		string = string[:x] + new_string+ string[x+len(old_string):]

	return string



print (replace("ABACATEIRO","A","J"))


"""
joao  -->>> indíce 2 - >>> string[:2] + new_string + string[3:]  len(old_string) = 1
joao ->>> indíce 0 - >>> string[:0] + new_string + string[2:]   len(old_string) = 2
"""