from tkinter import *
import random

root = Tk()
root.geometry("1366x768+0+0")
root.title("Implementações de I.A")

saida = StringVar()
operator = ""
Tops = Frame(root, width = 1366, height = 50, bg="powder blue", relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 600, height=400, relief = SUNKEN)
f2 = Frame(root, width = 600, height=200, pady = 50, relief = SUNKEN)
f3 = Frame(f1, width = 50, height=700, padx = 50, pady=50, relief = SUNKEN)
f4 = Frame(f1, width = 50, height=700, pady = 50, relief = SUNKEN)
f5 = Frame(f1, width = 50, height=700, pady = 50, relief = SUNKEN)
f6 = Frame(f1, width = 50, height=700, pady = 50, relief = SUNKEN)
f7 = Frame(f1, width = 50, height=700, pady = 50, relief = SUNKEN)

f1.pack(side = LEFT)
f2.pack(side = TOP)

f3.grid(row=0, column=0)
f4.grid(row=0, column=0)
f5.grid(row=0, column=0)
f6.grid(row=0, column=0)
f7.grid(row=0, column=0)

#===================================Info=======================================
lblInfo = Label(Tops, font=('arial', 50, 'bold'), text = "Implementações de I.A",
                    fg="Steel Blue", bd = 10, anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label(Tops, font=('arial', 20, 'bold'), text = "Algoritmos",
                    fg="Steel Blue", bd = 10, anchor='w')
lblInfo.grid(row=1, column=0)
#================================Funções===================================

def raise_frame(frame):
	frame.tkraise()

def impl1():
	saida.set("""Custo Uniforme\nBucharest->Fagaras->""")
	
def impl2():
	saida.set("""Busca Bidirecional\nBucharest->Sibiu""")
	
def impl3():
	saida.set("""Heurística\nBucharest->Oradea""")
	
def impl4():
	saida.set("""Busca A*\nBucharest->Timisoara""")

def qExit():
	root.destroy()

def Reset():
	pass

#----------- Label de Saída---------------
lblSaida = Label(f2, textvariable = saida, font = ("arial", 30), fg = "black", 
					padx = 200, width = 15, height = 12, bg = "white", justify = "left", anchor=NE).pack(side = LEFT)


#====================================Tela f3========================================

btn1=Button(f3, padx=40, pady=30, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Custo Uniforme", bg="powder blue", command = lambda:raise_frame(f4)).grid(row=0, column=0)
				
btn2=Button(f3, padx=40, pady=30, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Busca Bidirecional", bg="powder blue", command = lambda:raise_frame(f5)).grid(row=0, column=1)

btn3=Button(f3, padx=40, pady=30, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Heurística", bg="powder blue", command = lambda:raise_frame(f6)).grid(row=1, column=0)
				
btn4=Button(f3, padx=40, pady=30, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Busca A*", bg="powder blue", command = lambda:raise_frame(f7)).grid(row=1, column=1)										


#====================================Tela f4==========================================


romenia = IntVar()

cbRomenia = Checkbutton(f4, text="Mapa da Romenia", font = ("arial", 16, "bold"), variable=romenia)
cbRomenia.grid(row=0, column=0)

aspirador = IntVar()

cbAspirador = Checkbutton(f4, text="Aspirador de Pó", font = ("arial", 16, "bold"), variable=aspirador)
cbAspirador.grid(row=0, column=1)

Label(f4, text = "           ").grid(row=1, column=0)

lblInicio = Label(f4, text = "Início: ", font = ("arial", 20, "bold")).grid(row=2, column=0)
entryInicio = Entry(f4, font = ("arial", 18)).grid(row=2, column=1)

Label(f4, text = "           ").grid(row=3, column=0)

lblObjetivo = Label(f4, text = "Objetivo: ", font = ("arial", 20, "bold")).grid(row=4, column=0)
entryObjetivo = Entry(f4, font = ("arial", 18)).grid(row=4, column=1)

Label(f4, text = "           ").grid(row=5, column=0)
Label(f4, text = "           ").grid(row=6, column=0)

btnVoltar=Button(f4, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Voltar", bg="powder blue", command = lambda:raise_frame(f3)).grid(row=7, column=0)
				
btnCalcular=Button(f4, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Calcular", bg="powder blue", command = impl1).grid(row=7, column=1)

#====================================Tela f5==========================================


romenia5 = IntVar()

cbRomenia5 = Checkbutton(f5, text="Mapa da Romenia", font = ("arial", 16, "bold"), variable=romenia5)
cbRomenia5.grid(row=0, column=0)

aspirador5 = IntVar()

cbAspirador5 = Checkbutton(f5, text="Aspirador de Pó", font = ("arial", 16, "bold"), variable=aspirador5)
cbAspirador5.grid(row=0, column=1)

Label(f5, text = "           ").grid(row=1, column=0)

lblInicio5 = Label(f5, text = "Início: ", font = ("arial", 20, "bold")).grid(row=2, column=0)
entryInicio5 = Entry(f5, font = ("arial", 18)).grid(row=2, column=1)

Label(f5, text = "           ").grid(row=3, column=0)

lblObjetivo5 = Label(f5, text = "Objetivo: ", font = ("arial", 20, "bold")).grid(row=4, column=0)
entryObjetivo5 = Entry(f5, font = ("arial", 18)).grid(row=4, column=1)

Label(f5, text = "           ").grid(row=5, column=0)
Label(f5, text = "           ").grid(row=6, column=0)

btnVoltar5=Button(f5, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Voltar", bg="powder blue", command = lambda:raise_frame(f3)).grid(row=7, column=0)
				
btnCalcular5=Button(f5, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Calcular", bg="powder blue", command = impl2).grid(row=7, column=1)
				
#====================================Tela f6==========================================


romenia6 = IntVar()

cbRomenia6 = Checkbutton(f6, text="Mapa da Romenia", font = ("arial", 16, "bold"), variable=romenia6)
cbRomenia6.grid(row=0, column=0)

aspirador6 = IntVar()

cbAspirador6 = Checkbutton(f6, text="Aspirador de Pó", font = ("arial", 16, "bold"), variable=aspirador6)
cbAspirador6.grid(row=0, column=1)

Label(f6, text = "           ").grid(row=1, column=0)

lblInicio6 = Label(f6, text = "Início: ", font = ("arial", 20, "bold")).grid(row=2, column=0)
entryInicio6 = Entry(f6, font = ("arial", 18)).grid(row=2, column=1)

Label(f6, text = "           ").grid(row=3, column=0)

lblObjetivo6 = Label(f6, text = "Objetivo: ", font = ("arial", 20, "bold")).grid(row=4, column=0)
entryObjetivo6 = Entry(f6, font = ("arial", 18)).grid(row=4, column=1)

Label(f6, text = "           ").grid(row=5, column=0)
Label(f6, text = "           ").grid(row=6, column=0)

btnVoltar6=Button(f6, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Voltar", bg="powder blue", command = lambda:raise_frame(f3)).grid(row=7, column=0)
				
btnCalcular6=Button(f6, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Calcular", bg="powder blue", command = impl3).grid(row=7, column=1)


#====================================Tela f7==========================================


romenia7 = IntVar()

cbRomenia7 = Checkbutton(f7, text="Mapa da Romenia", font = ("arial", 16, "bold"), variable=romenia7)
cbRomenia7.grid(row=0, column=0)

aspirador7 = IntVar()

cbAspirador7 = Checkbutton(f7, text="Aspirador de Pó", font = ("arial", 16, "bold"), variable=aspirador7)
cbAspirador7.grid(row=0, column=1)

Label(f7, text = "           ").grid(row=1, column=0)

lblInicio7 = Label(f7, text = "Início: ", font = ("arial", 20, "bold")).grid(row=2, column=0)
entryInicio7 = Entry(f7, font = ("arial", 18)).grid(row=2, column=1)

Label(f7, text = "           ").grid(row=3, column=0)

lblObjetivo7 = Label(f7, text = "Objetivo: ", font = ("arial", 20, "bold")).grid(row=4, column=0)
entryObjetivo7 = Entry(f7, font = ("arial", 18)).grid(row=4, column=1)

Label(f7, text = "           ").grid(row=5, column=0)
Label(f7, text = "           ").grid(row=6, column=0)

btnVoltar7=Button(f7, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Voltar", bg="powder blue", command = lambda:raise_frame(f3)).grid(row=7, column=0)
				
btnCalcular7=Button(f7, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Calcular", bg="powder blue", command = impl4).grid(row=7, column=1)


raise_frame(f3)

root.mainloop()







