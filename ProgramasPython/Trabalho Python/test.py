## Programa Gênio Quiz

#importando a interface grafica(tkinter)
from tkinter import *

### Fontes ###
def fontes(letra, tamanho):
	return (letra, tamanho, 'bold')
#criando a janela
instancia_Tk = Tk()

#Carregando imagem
imagem = PhotoImage(file = "twice.gif")

#Título
instancia_Tk.title("Genio Quiz JDK")

#especificando o tamanho da janela
instancia_Tk.geometry('1040x500')
#deixando a tela em tamanho fixo
instancia_Tk.resizable(width=False, height=False)


def show_frame(frame):
	frame.tkraise()

#funcao principal

def main():

	arquivo = open("perguntas.txt", "r")
	perguntas = arquivo.read().split("\n")

	arquivo.close()

	arquivo = open("respostas.txt", "r")
	respostas = arquivo.read().split("\n")

	arquivo.close()

	instrucao = "Ta afim de moleza? \nNa minha época era descobrindo na raça!!! \nEssa geração de leite com pêra"
	credito= "Este jogo foi feito para o trabalho de python.\n 1°Semestre\nFeito por: Jessica, Diego e Fabiola\nJogo Inspirado no Genio Quiz de André B*******"	

	frames ={}
	sub_frames = {}

	valor_da_subframe = 1
	valor = 0

	frames['fi'] = Frame(instancia_Tk)	
	frames['ff'] = Frame(instancia_Tk)
	frames['fc'] = Frame(instancia_Tk)
	frames['fv'] = Frame(instancia_Tk)


	for x in range(1, 17):
		frames['f%i'%(x)] = Frame(instancia_Tk)
		if x>=2:
			sub_frames['s%i'%(valor_da_subframe)] = Frame(frames['f%i'%(x)])
			sub_frames['s%i'%(valor_da_subframe)].pack()  #s1
			sub_frames['s%i'%(valor_da_subframe+1)] = Frame(frames['f%i'%(x)])
			sub_frames['s%i'%(valor_da_subframe+1)].pack()
			if valor_da_subframe == 9:
				subFrame4 = Frame(frames['f4'], padx = '20')
				Label(subFrame4, text = "Fabiola manicure", image = imagem).pack()
				subFrame4.pack()	
			sub_frames['s%i'%(valor_da_subframe+2)] = Frame(frames['f%i'%(x)])
			sub_frames['s%i'%(valor_da_subframe+2)].pack()
			sub_frames['s%i'%(valor_da_subframe+3)] = Frame(frames['f%i'%(x)])
			sub_frames['s%i'%(valor_da_subframe+3)].pack()

			feito_por =  Label (sub_frames['s%i'%(valor_da_subframe + 3)], text = "Jessica, Diego e Fabiola", font = ("Verdana", "13", "italic"), pady = '250').pack(side = 'left')

			if valor != 14:
				if valor != 9 and valor != 10:
					if valor == 2:
						print (valor_da_subframe)
					numero_pergunta = Button (sub_frames['s%i'%(valor_da_subframe)], text = '%i - '%(valor+1), height = '1', width = '3', font = ("Verdana", "13"), command = lambda: show_frame(frames['ff']), relief = FLAT).pack(side = "left")
				pergunta = Label (sub_frames['s%i'%(valor_da_subframe)], text = perguntas[valor], font = fontes("Verdana", '14'), pady = '50').pack(side = 'left')
			valor+=1
			valor_da_subframe += 4


	# Sub - Frames para botões 
	subFrame1 = Frame(frames['f1'], padx = '20', pady = '10')
	subFrame2 = Frame(frames['f1'], padx = '20', pady = '20')
	subFrame3 = Frame(frames['f2'], padx = '20')
	subFrame4 = Frame(frames['f4'], padx = '20')

	numero_pergunta = Button (sub_frames['s57'], text = '15 - ', height = '1', width = '3', font = ("Verdana", "13"), command = lambda: show_frame(frames['fv']), relief = FLAT).pack(side = "left")
	pergunta = Label (sub_frames['s57'], text = perguntas[14], font = fontes("Verdana", '14'), pady = '50').pack(side = 'left')

	

	

	for frame in frames.values():
	    frame.grid(row=0, column=0, sticky='news')

	frames['fi'].grid(row=0, column=0, sticky='news')
	frames['ff'].grid(row=0, column=0, sticky='news')
	frames['fc'].grid(row=0, column=0, sticky='news')
	frames['fv'].grid(row=0, column=0, sticky='news')

	menu = LabelFrame(frames['f1'], text = 'Menu', height = '20').pack()

	### CRIANDO TELA INICIAL ###

	inicio = Label (frames['f1'], text = "GENIO QUIZ", font = fontes("Verdana", '50'), fg = "gray", pady = '50', padx = '50').pack()

	jogar = Button (subFrame1, text = "JOGAR", font = ("Verdana", '16', "bold"), padx = "35",  fg = 'green', command = lambda: show_frame(frames['f2'])).pack(side = "left")
	instrucoes = Button (subFrame1, text = "INSTRUÇÕES", padx = "35", font = ("Verdana", '16', "bold"), fg = "red", command = lambda: show_frame(frames['fi']) ).pack(side = "left")
	creditos = Button (subFrame1, text = "CRÉDITOS", padx = "35", font = ("Verdana", '16', "bold"), fg = "blue", command = lambda: show_frame(frames['fc']) ).pack()
	
	### CRIANDO TELA DE CRÉDITOS ###
	Label (frames['fc'], text = "CRÉDITOS", font = fontes("Verdana", '50'), fg = "blue", pady = '50', padx = '70').pack()
	Label (frames['fc'], text = credito, font = fontes("Verdana", '16')).pack()
	voltar = Button (frames['fc'], text = "VOLTAR", padx = "100", font = ("Verdana", '16', "bold"), pady = '25', fg = 'green', command = lambda: show_frame(frames['f1'])).pack()

	### CRIANDO TELA DE VITÓRIA ###
	Label (frames['fv'], text = "VITÓRIA !!!", font = fontes("Verdana", '50'), fg = "red", pady = '50', padx = '50').pack()
	jogar_novamente = Button (frames['fv'], text = "JOGAR NOVAMENTE", font = ("Verdana", '16', "bold"), fg = 'blue', command = lambda: show_frame(frames['f1'])).pack()

	### TELA DE INSTRUÇÕES ###
	Label (frames['fi'], text = "INSTRUÇÕES", font = fontes("Verdana", '50'), fg = "blue", pady = '50', padx = '70').pack()
	Label (frames['fi'], text = instrucao, font = fontes("Verdana", '16'), pady = "20").pack()
	voltar = Button (frames['fi'], text = "VOLTAR", padx = "100", font = ("Verdana", '16', "bold"), pady = '25', fg = 'green', command = lambda: show_frame(frames['f1'])).pack()

	### Tela FINAL ###
	Label (frames['ff'], text = "DERROOOTAAAAAAAAAAA", fg = "#400080",pady = '100',font = ("Corsola", '50','bold','italic')).pack()
	Button (frames['ff'], text = "RECOMEÇAR", fg = "#276DD8", font = fontes("Verdana", '16'), command = lambda: show_frame(frames['f1'])).pack()

	### ADICIONANDO BOTÕES NAS FRAMES ###
	x = 2
	valor_resp = 0
	# 1 Pergunta
	Button(sub_frames['s%i'%(x)], text = respostas[valor_resp], bg = "blue", fg = 'white', padx = '60', font = ("Verdana", "13"), command = lambda: show_frame(frames['ff'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", fg = 'white', padx = '75',font = ("Verdana", "13"), command = lambda: show_frame(frames['f3'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['ff'])).pack()
	x +=4
	valor_resp+=5

	#2 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['ff'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['f4'])).pack()
	x +=4
	valor_resp+=5

	#3 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['ff'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['f5'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text = respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['ff'])).pack()

	x +=4
	valor_resp+=5

	#4 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['ff'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['f6'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['ff'])).pack()

	x +=4
	valor_resp+=5

	#5 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['ff'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['f7'])).pack()

	x +=4
	valor_resp+=5

	#6 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['f8'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['ff'])).pack()

	x +=4
	valor_resp+=5

	#7 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['f9'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['ff'])).pack()

	x +=4
	valor_resp+=5

	#8 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['ff'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text = respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['f10'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['ff'])).pack()
	x +=4
	valor_resp+=5

	#9 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['f11'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text = respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['ff'])).pack()

	x +=4
	valor_resp+=5

	#10 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['ff'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['f12'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['ff'])).pack()

	x +=4
	valor_resp+=5

	#11 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['f13'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['ff'])).pack()

	x +=4
	valor_resp+=5

	#12 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['ff'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['f14'])).pack()

	x +=4
	valor_resp+=5

	#13 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['ff'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['f15'])).pack()
	x +=4
	valor_resp+=5

	#14 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['ff'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['f16'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['ff'])).pack()
	x +=4
	valor_resp+=5

	#15 Pergunta

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '60', command = lambda: show_frame(frames['ff'])).pack(side = "left")

	Button(sub_frames['s%i'%(x)], text =  respostas[valor_resp + 1], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '75', command = lambda: show_frame(frames['ff'])).pack()

	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 2], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '68', command = lambda: show_frame(frames['ff'])).pack(side = "left")
	Button(sub_frames['s%i'%(x+1)], text =  respostas[valor_resp + 3], bg = "blue", font = ("Verdana", "13"), fg = 'white', padx = '69', command = lambda: show_frame(frames['ff'])).pack()


	#subFrame3.pack()
	#Label(subFrame4, text = "__________________", font = fontes("Verdana", '30')).pack()

	subFrame2.pack(pady = "30")
	subFrame1.pack()


	show_frame(frames['f1'])
	
#chamando a funcao principal
main()

#loop da janela
instancia_Tk.mainloop()