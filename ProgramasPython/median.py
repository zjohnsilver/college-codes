def median (lista):
    lista = sorted(lista)
    
    if (len(lista) % 2):
        return lista[len(lista)/2]
    else:
        return (lista[(len(lista)/2)-1] +  lista[len(lista)/2])/2.0


print median([4,5,5,4])
print median([1,2,2])