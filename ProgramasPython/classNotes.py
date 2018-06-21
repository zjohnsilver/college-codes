#!usr/bin/python
#coding=utf-8

qtd_alunos=input("Alunos: ")
aluno=1
cont=0
cont1=0
cont2=0
soma=0
x=qtd_alunos
while qtd_alunos>0:
	print "Aluno %i: "%(aluno)
	print "--------"
	nota1=input("Nota I: ")
	nota2=input("Nota II: ")
	media=(nota1+nota2)/2.0
	if media>=7:
		cont+=1
		print "Aluno %i aprovado!"%(aluno)
	if media<=3:
		cont1+=1
		print "Aluno %i reprovado!"%(aluno)
	if 3<media<7:
		cont2+=1
		print "Aluno %i recuperação"%(aluno)
	soma=soma+media
	aluno+=1
	qtd_alunos-=1
	print "--------------------------------------------------------"
	print ""
		
print "Total de reprovados: %i"%(cont1)
print "Total de Aprovados: %i"%(cont)
print "Total de recuperação: %i"%(cont2)

print "A média da classe: %i"%(soma/x)


#Lancelot

