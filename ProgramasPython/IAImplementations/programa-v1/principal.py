from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from buscaCustoUniforme import buscaUniforme
from buscaGulosa import buscaGulosa
from buscaEstrela import buscaA
from BuscaBidirecional import busca_bidirecional

root = Tk()
root.geometry("1366x768+0+0")
root.title("Implementações de I.A")

saida = StringVar()
operator = ""
aspirador = IntVar()
Tops = Frame(root, width = 1366, height = 50, bg="powder blue", relief = SUNKEN)
Tops.pack(side = TOP)

f1 = Frame(root, width = 600, height=400, relief = SUNKEN)
f2 = Frame(root, width = 600, height=200, pady = 50, relief = SUNKEN)
f3 = Frame(f1, width = 50, height=700, padx = 50, pady=100, relief = SUNKEN)
f4 = Frame(f1, width = 50, height=700, pady = 50, padx = 50, relief = SUNKEN)
f5 = Frame(f1, width = 50, height=700, pady = 50, padx = 50, relief = SUNKEN)
f6 = Frame(f1, width = 50, height=700, pady = 50, padx = 50, relief = SUNKEN)
f7 = Frame(f1, width = 50, height=700, pady = 50, padx = 50, relief = SUNKEN)

f4Aspirador = Frame(f1, width = 50, height=700, pady = 50, relief = SUNKEN)
f5Aspirador = Frame(f1, width = 50, height=700, pady = 50, relief = SUNKEN)
f6Aspirador = Frame(f1, width = 50, height=700, pady = 50, relief = SUNKEN)
f7Aspirador = Frame(f1, width = 50, height=700, pady = 50, relief = SUNKEN)

f1.pack(side = LEFT)
f2.pack(side = TOP)

f3.grid(row=0, column=0)
f4.grid(row=0, column=0)
f5.grid(row=0, column=0)
f6.grid(row=0, column=0)
f7.grid(row=0, column=0)

f4Aspirador.grid(row=0, column=0)
f5Aspirador.grid(row=0, column=0)
f6Aspirador.grid(row=0, column=0)
f7Aspirador.grid(row=0, column=0)

#===================================Info=======================================
lblInfo = Label(Tops, font=('arial', 50, 'bold'), text = "Implementações de I.A",
                    fg="Steel Blue", bd = 10, anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label(Tops, font=('arial', 20, 'bold'), text = "Algoritmos",
                    fg="Steel Blue", bd = 10, anchor='w')
lblInfo.grid(row=1, column=0)

#========================== Variaveis ComboBox =================================
## Variaveis da tela Custo Uniforme
comboBoxInicio = StringVar()
comboBoxObjetivo = StringVar()

## Variaveis da tela Busca Bidirecional
comboBox1 = StringVar()
comboBox2 = StringVar()

#================================Funções===================================

def raise_frame(frame):
	frame.tkraise()
	
def ajustarSaida(strSaida):
	count = 0
	newSaida = ""
	for i in strSaida:
		newSaida += i + " => "
	
	new = " "
		
	for i in newSaida:
		new += i
		if i == ">":
			count+=1
		if count==2:
			new+="\n"
			count=0
	return new

def impl1():
	solucao = ""
	if aspirador.get() == 0: ## Romenia
		try:
			solucao = buscaUniforme(False, comboBoxInicio.get(), comboBoxObjetivo.get())
			if solucao!="Falha":
				newSolucao = ajustarSaida(solucao)
				saida.set(newSolucao)
			else:
				saida.set("FALHA")
		except:
			messagebox.showerror("Erro", "Inicio errado")
	
	if aspirador.get() == 1:
		try:
			solucao = buscaUniforme(True, comboBoxInicio.get())
			if solucao!="Falha":
				newSolucao = ajustarSaida(solucao)
				saida.set(newSolucao)
			else:
				saida.set("FALHA")
		except:
			messagebox.showerror("Erro", "Inicio errado")
	
def impl2():
	if comboBox1 == "DFS":
		dfs = True
	else:
		dfs = False
	
	if comboBox2 == "DFS":
		dfs2 = True
	else:
		dfs2 = False	
	
	
	solucao = ""
	if aspirador.get() == 0: ## Romenia
		try:
			solucao = busca_bidirecional(False, comboBoxInicio.get(), dfs, dfs2, comboBoxObjetivo.get())
			if solucao!="Falha":
				newSolucao = ajustarSaida(solucao)
				saida.set(newSolucao)
			else:
				saida.set("FALHA")
		except:
			messagebox.showerror("Erro", "Inicio errado")
	
	if aspirador.get() == 1:
		try:
			solucao = busca_bidirecional(True, comboBoxInicio.get(), dfs, dfs2)
			if solucao!="Falha":
				newSolucao = ajustarSaida(solucao)
				saida.set(newSolucao)
			else:
				saida.set("FALHA")
		except:
			messagebox.showerror("Erro", "Inicio errado")
	
def impl3():
	### Busca Gulosa
	solucao = ""
	try:
		solucao = buscaGulosa(comboBoxInicio	.get())
		if solucao!="Falha":
			newSolucao = ajustarSaida(solucao)
			saida.set(newSolucao)
		else:
			saida.set("FALHA")
	except:
		messagebox.showerror("Erro", "Inicio errado")
	
	
def impl4():
	solucao = ""
	try:
		solucao = buscaA(comboBoxInicio.get())
		if solucao!="Falha":
			newSolucao = ajustarSaida(solucao)
			saida.set(newSolucao)
		else:
			saida.set("FALHA")
	except:
		messagebox.showerror("Erro", "Inicio errado")
	
def ir_para_Tela(tela, aspira):
	aspirador.set(aspira)
	comboBoxInicio.set("")
	comboBoxObjetivo.set("")
	comboBox1.set("")
	comboBox2.set("")
	raise_frame(tela)
	
def voltar():
	raise_frame(f3)
	
	## Tela Custo Uniforme
	comboBox1.set("")
	comboBox2.set("")
	comboBoxInicio.set("")
	comboBoxObjetivo.set("")
	saida.set("")

#----------- Label de Saída---------------
lblSaida = Label(f2, textvariable = saida, font = ("arial", 30), fg = "black", 
					padx = 200, width = 15, height = 12, bg = "white", justify = "left", anchor=NE).pack(side = LEFT)


#====================================Tela f3========================================

btn1=Button(f3, padx=40, pady=30, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Custo Uniforme", bg="powder blue", command = lambda:raise_frame(f4)).grid(row=0, column=0)
				
btn2=Button(f3, padx=40, pady=30, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Busca Bidirecional", bg="powder blue", command = lambda:raise_frame(f5)).grid(row=0, column=1)

btn3=Button(f3, padx=40, pady=30, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Busca Gulosa", bg="powder blue", command = lambda:raise_frame(f6)).grid(row=1, column=0)
				
btn4=Button(f3, padx=40, pady=30, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Busca A*", bg="powder blue", command = lambda:raise_frame(f7)).grid(row=1, column=1)	

Label(f3, text = "          ").grid(row=2, column=0)									


#====================================Tela f4 (Busca Custo Uniforme)==========================================
Button(f4, text="Aspirador", padx=16, pady=10, bd=16, fg="black", font=("arial", 14, "bold"), width=10, 
					command= lambda:ir_para_Tela(f4Aspirador, 1)).grid(row=0, column=0)
					
Label(f4, text = "Romenia", font=("arial", 16, "bold")).grid(row=0, column = 1)

Label(f4, text = "           ").grid(row=1, column=0)

Label(f4, text = "Início: ", font = ("arial", 20, "bold")).grid(row=2, column=0)
ttk.Combobox(f4, textvariable = comboBoxInicio, font = ("arial", 18), height = 10,
						   values = ('Arad', 'Bucharest', 'Craivoa', 'Dobreta', 'Eforie', 'Fagaras', 'Giurgiu',
									 'Hirsova', 'Iasi', 'Lugoj', 'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu',
									 'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui', 'Zerind')).grid(row=2, column=1)

Label(f4, text = "           ").grid(row=3, column=0)

Label(f4, text = "Objetivo: ", font = ("arial", 20, "bold")).grid(row=4, column=0)
ttk.Combobox(f4, textvariable = comboBoxObjetivo, font = ("arial", 18), height = 10, 
							 values = ('Arad', 'Bucharest', 'Craivoa', 'Dobreta', 'Eforie', 'Fagaras', 'Giurgiu',
									   'Hirsova', 'Iasi', 'Lugoj', 'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu',
									   'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui', 'Zerind')).grid(row=4, column=1)

Label(f4, text = "           ").grid(row=5, column=0)
Label(f4, text = "           ").grid(row=6, column=0)

Button(f4, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Voltar", bg="powder blue", command = voltar).grid(row=7, column=0)
				
Button(f4, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Calcular", bg="powder blue", command = impl1).grid(row=7, column=1)
				
################################### Tela f4 ASPIRADOR #########################################
Button(f4Aspirador, text="Romenia", padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10, 
					command=lambda:ir_para_Tela(f4, 0)).grid(row=0, column=0)
					
Label(f4Aspirador, text = "Aspirador", font=("arial", 16, "bold")).grid(row=0, column = 1)

Label(f4Aspirador, text = "           ").grid(row=1, column=0)

Label(f4Aspirador, text = "Início: ", font = ("arial", 20, "bold")).grid(row=2, column=0)
ttk.Combobox(f4Aspirador, textvariable = comboBoxInicio, font = ("arial", 18), height = 10,
						   values = ('ESS', 'DSS', 'ESL', 'ELS', 'DLS', 'DSL')).grid(row=2, column=1)

Label(f4Aspirador, text = "           ").grid(row=3, column=0)

Label(f4Aspirador, text = "           ").grid(row=5, column=0)

Button(f4Aspirador, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Voltar", bg="powder blue", command = voltar).grid(row=6, column=0)
				
Button(f4Aspirador, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Calcular", bg="powder blue", command = impl1).grid(row=6, column=1)

#====================================Tela f5 (Busca Bidirecional)==========================================

Button(f5, text="Aspirador", padx=16, pady=10, bd=16, fg="black", font=("arial", 14, "bold"), width=10, 
					command= lambda:ir_para_Tela(f5Aspirador, 1)).grid(row=0, column=0)
					
Label(f5, text = "Romenia", font=("arial", 16, "bold")).grid(row=0, column = 1)

Label(f5, text = "           ").grid(row=1, column=0)

lblBusca1 = Label(f5, text = "Busca I: ", font = ("arial", 20, "bold")).grid(row=2, column=0)
comboBoxBusca1 = ttk.Combobox(f5, textvariable = comboBox1, font = ("arial", 18), values = ("DFS", "BFS")).grid(row=2, column=1)

lblBusca2 = Label(f5, text = "Busca II: ", font = ("arial", 20, "bold")).grid(row=3, column=0)
comboBoxBusca2 = ttk.Combobox(f5, textvariable = comboBox2, font = ("arial", 18), values = ("DFS", "BFS")).grid(row=3, column=1)

Label(f5, text = "           ").grid(row=4, column=0)

lblInicio5 = Label(f5, text = "Início: ", font = ("arial", 20, "bold")).grid(row=5, column=0)
boxInicio5 = ttk.Combobox(f5, textvariable = comboBoxInicio, font = ("arial", 18), height = 10, 
							 values = ('Arad', 'Bucharest', 'Craivoa', 'Dobreta', 'Eforie', 'Fagaras', 'Giurgiu',
									   'Hirsova', 'Iasi', 'Lugoj', 'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu',
									   'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui', 'Zerind')).grid(row=5, column=1)

Label(f5, text = "           ").grid(row=6, column=0)

lblObjetivo5 = Label(f5, text = "Objetivo: ", font = ("arial", 20, "bold")).grid(row=7, column=0)
boxObjetivo5 = ttk.Combobox(f5, textvariable = comboBoxObjetivo, font = ("arial", 18), height = 10, 
							 values = ('Arad', 'Bucharest', 'Craivoa', 'Dobreta', 'Eforie', 'Fagaras', 'Giurgiu',
									   'Hirsova', 'Iasi', 'Lugoj', 'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu',
									   'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui', 'Zerind')).grid(row=7, column=1)

Label(f5, text = "           ").grid(row=8, column=0)
Label(f5, text = "           ").grid(row=9, column=0)

btnVoltar5=Button(f5, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Voltar", bg="powder blue", command = voltar).grid(row=10, column=0)
				
btnCalcular5=Button(f5, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Calcular", bg="powder blue", command = impl2).grid(row=10, column=1)
				
				
################################### Tela f5 ASPIRADOR #########################################
Button(f5Aspirador, text="Romenia", padx=16, pady=10, bd=16, fg="black", font=("arial", 14, "bold"), width=10, 
					command= lambda:ir_para_Tela(f5, 0)).grid(row=0, column=0)
					
Label(f5Aspirador, text = "Aspirador", font=("arial", 16, "bold")).grid(row=0, column = 1)

Label(f5Aspirador, text = "           ").grid(row=1, column=0)

lblBusca1 = Label(f5Aspirador, text = "Busca I: ", font = ("arial", 20, "bold")).grid(row=2, column=0)
comboBoxBusca1 = ttk.Combobox(f5Aspirador, textvariable = comboBox1, font = ("arial", 18), values = ("DFS", "BFS")).grid(row=2, column=1)

lblBusca2 = Label(f5Aspirador, text = "Busca II: ", font = ("arial", 20, "bold")).grid(row=3, column=0)
comboBoxBusca2 = ttk.Combobox(f5Aspirador, textvariable = comboBox2, font = ("arial", 18), values = ("DFS", "BFS")).grid(row=3, column=1)

Label(f5Aspirador, text = "           ").grid(row=4, column=0)

lblInicio5 = Label(f5Aspirador, text = "Início: ", font = ("arial", 20, "bold")).grid(row=5, column=0)
boxInicio5 = ttk.Combobox(f5Aspirador, textvariable = comboBoxInicio, font = ("arial", 18), height = 10,
						   values = ('ESS', 'DSS', 'ESL', 'ELS', 'DLS', 'DSL')).grid(row=5, column=1)

Label(f5Aspirador, text = "           ").grid(row=6, column=0)

Label(f5Aspirador, text = "           ").grid(row=8, column=0)

btnVoltar5=Button(f5Aspirador, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Voltar", bg="powder blue", command = voltar).grid(row=9, column=0)
				
btnCalcular5=Button(f5Aspirador, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Calcular", bg="powder blue", command = impl2).grid(row=9, column=1)

#====================================Tela f6==========================================
					
Label(f6, text = " Busca Gulosa ", font=("arial", 20, "bold"), relief = GROOVE).grid(row=0, column = 0)

Label(f6, text = "           ").grid(row=1, column=0)

Label(f6, text = "Início: ", font = ("arial", 20, "bold")).grid(row=2, column=0)
ttk.Combobox(f6, textvariable = comboBoxInicio, font = ("arial", 18), height = 10, 
							 values = ('Arad', 'Bucharest', 'Craivoa', 'Dobreta', 'Eforie', 'Fagaras', 'Giurgiu',
									   'Hirsova', 'Iasi', 'Lugoj', 'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu',
									   'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui', 'Zerind')).grid(row=2, column=1)

Label(f6, text = "           ").grid(row=3, column=0)

Button(f6, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Voltar", bg="powder blue", command = voltar).grid(row=7, column=0)
				
Button(f6, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Calcular", bg="powder blue", command = impl3).grid(row=7, column=1)

#====================================Tela f7==========================================

Label(f7, text = " Busca A* ", font=("arial", 20, "bold"), relief = GROOVE).grid(row=0, column = 0)

Label(f7, text = "           ").grid(row=1, column=0)

lblInicio7 = Label(f7, text = "Início: ", font = ("arial", 20, "bold")).grid(row=2, column=0)
boxInicio7 = ttk.Combobox(f7, textvariable = comboBoxInicio, font = ("arial", 18), height = 10, 
							 values = ('Arad', 'Bucharest', 'Craivoa', 'Dobreta', 'Eforie', 'Fagaras', 'Giurgiu',
									   'Hirsova', 'Iasi', 'Lugoj', 'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu',
									   'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui', 'Zerind')).grid(row=2, column=1)

Label(f7, text = "           ").grid(row=3, column=0)
Label(f7, text = "           ").grid(row=4, column=0)

btnVoltar7=Button(f7, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Voltar", bg="powder blue", command = voltar).grid(row=5, column=0)
				
btnCalcular7=Button(f7, padx=16, pady=16, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
				text = "Calcular", bg="powder blue", command = impl4).grid(row=5, column=1)


raise_frame(f3)

root.mainloop()
