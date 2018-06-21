############################# Makefile ##########################
#Nome do executavel
all: main.e
# Cria dois arquivos .o (objetos)
# O compilador faz a ligação entre os dois objetos
main.e: funcoes.o main.o 
	gcc -o main.e funcoes.o main.o -lm

# funcoes.o (destino), funcoes.c (origem)
funcoes.o: funcoes.c funcoes.h
	gcc -o funcoes.o -c funcoes.c -lm
main.o: main.c funcoes.h
	gcc -o main.o -c main.c -lm

#Se digitar make clean no terminal, ele deleta os arquivos .o (objetos)
clean:
	rm -rf *.o

#Digite make mrproper para apagar todos os arquivos objetos e executaveis
mrproper: clean
	rm -rf main.e
