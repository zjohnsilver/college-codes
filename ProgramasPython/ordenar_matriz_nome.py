# Ordenar uma matriz pelos nomes dos usuarios 

# Created by Jon in 18.06.2016

def main():
	a = [['Joao', 1500, 25],
		 ['Pedro', 1700, 30],
		 ['Amanda', 2000, 27]]

	for i in range(0, 2):
		for j in range (1, 3):
			if a[i][0] > a[j][0]:
				aux = a[i]
				a[i] = a[j]
				a[j] = aux

	print (a)


main()