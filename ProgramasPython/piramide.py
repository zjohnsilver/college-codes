## PROGRAM PYTHON


def main():
	valor = input()
	imprimir = ""

	for x in range(1, valor+1):
		for y in range(1, x+1):
			imprimir += str(y) + " "
		print imprimir
		imprimir = ""
	




main()