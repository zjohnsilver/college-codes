arquivo = open("arqlista.txt", "w")

lista = ["1", "2", "3", "4"]

arquivo.writelines("/".join(lista))

arquivo.close()