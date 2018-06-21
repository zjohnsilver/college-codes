arquivo = open("Destino do arquivo exp: ('/home/thiago/dados','w')

arquivo.write('5\n')
arquivo.write('6\n')

arquivo = open("Destino do arquivo exp: ('/home/thiago/dados','r')

s1 = arquivo.readline()
s2 = arquivo.readline()

print s1
print s2

arquivo.close()
