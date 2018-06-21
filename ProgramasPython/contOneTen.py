
arquivo = open("Contagemde1a10.txt" , "w")

for x in range(11):

	arquivo.write(str(x)+"\n")


arquivo.close()

arquivo = open("Contagemde1a10.txt" , "r")

print (arquivo.read())

arquivo.close()


