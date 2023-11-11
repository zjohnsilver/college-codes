#######################################
# JOGO DA VELHA COM INTERFACE GRAFICA #
#                                     #
# João Carlos                15/11/16 #
#######################################


from tkinter import Button, Frame, Label, Tk

# criando a janela
instancia_Tk = Tk()


# Titulo
instancia_Tk.title("Jogo da Velha")

# especificando o tamanho da janela
instancia_Tk.geometry("550x400")

# deixando a tela em tamanho fixo
instancia_Tk.resizable(width=False, height=False)


class Game:
    def __init__(self, instancia):
        self.sub_frames = {}
        self.buttons = {}

        self.gameFrame = Frame(instancia)
        self.victory = Frame(instancia)

        self.gameFrame.grid(row=0, column=0, sticky="news")
        self.victory.grid(row=0, column=0, sticky="news")

        self.test = True

        x = 0

        self.sub_frames["f%i" % (x)] = Frame(self.gameFrame)
        self.sub_frames["f%i" % (x + 1)] = Frame(self.gameFrame)
        self.sub_frames["f%i" % (x + 2)] = Frame(self.gameFrame)

        self.sub_frames["f%i" % (x)].pack()
        self.sub_frames["f%i" % (x + 1)].pack()
        self.sub_frames["f%i" % (x + 2)].pack()

        x = 0

        self.labelVictory = Label(self.victory, text="VITÓRIAA!!!!").pack()

        self.label = Label(
            self.sub_frames["f0"], text="", font=("Verdana", "27")
        ).pack()

        self.b1 = Button(
            self.sub_frames["f%i" % (x)],
            text="  ",
            font=("Verdana", "50", "bold"),
            padx="35",
            fg="blue",
            command=self.click_b1,
        )
        self.b2 = Button(
            self.sub_frames["f%i" % (x)],
            text="  ",
            font=("Verdana", "50", "bold"),
            padx="35",
            fg="blue",
            command=self.click_b2,
        )
        self.b3 = Button(
            self.sub_frames["f%i" % (x)],
            text="  ",
            font=("Verdana", "50", "bold"),
            padx="35",
            fg="blue",
            command=self.click_b3,
        )
        self.b4 = Button(
            self.sub_frames["f%i" % (x + 1)],
            text="  ",
            font=("Verdana", "50", "bold"),
            padx="35",
            fg="blue",
            command=self.click_b4,
        )
        self.b5 = Button(
            self.sub_frames["f%i" % (x + 1)],
            text="  ",
            font=("Verdana", "50", "bold"),
            padx="35",
            fg="blue",
            command=self.click_b5,
        )
        self.b6 = Button(
            self.sub_frames["f%i" % (x + 1)],
            text="  ",
            font=("Verdana", "50", "bold"),
            padx="35",
            fg="blue",
            command=self.click_b6,
        )
        self.b7 = Button(
            self.sub_frames["f%i" % (x + 2)],
            text="  ",
            font=("Verdana", "50", "bold"),
            padx="35",
            fg="blue",
            command=self.click_b7,
        )
        self.b8 = Button(
            self.sub_frames["f%i" % (x + 2)],
            text="  ",
            font=("Verdana", "50", "bold"),
            padx="35",
            fg="blue",
            command=self.click_b8,
        )
        self.b9 = Button(
            self.sub_frames["f%i" % (x + 2)],
            text="  ",
            font=("Verdana", "50", "bold"),
            padx="35",
            fg="blue",
            command=self.click_b9,
        )

        self.b1.pack(side="left")
        self.b2.pack(side="left")
        self.b3.pack(side="left")
        self.b4.pack(side="left")
        self.b5.pack(side="left")
        self.b6.pack(side="left")
        self.b7.pack(side="left")
        self.b8.pack(side="left")
        self.b9.pack(side="left")

        self.show_frame(self.gameFrame)

    def click_b1(self):
        if self.test:
            self.b1["text"] = "X"
            self.test = False
        else:
            self.b1["text"] = "O"
            self.test = True
        self.test_victory()

    def click_b2(self):
        if self.test:
            self.b2["text"] = "X"
            self.test = False
        else:
            self.b2["text"] = "O"
            self.test = True
        self.test_victory()

    def click_b3(self):
        if self.test:
            self.b3["text"] = "X"
            self.test = False
        else:
            self.b3["text"] = "O"
            self.test = True

    def click_b4(self):
        if self.test:
            self.b4["text"] = "X"
            self.test = False
        else:
            self.b4["text"] = "O"
            self.test = True
        self.test_victory()

    def click_b5(self):
        if self.test:
            self.b5["text"] = "X"
            self.test = False
        else:
            self.b5["text"] = "O"
            self.test = True
        self.test_victory()

    def click_b6(self):
        if self.test:
            self.b6["text"] = "X"
            self.test = False
        else:
            self.b6["text"] = "O"
            self.test = True
        self.test_victory()

    def click_b7(self):
        if self.test:
            self.b7["text"] = "X"
            self.test = False
        else:
            self.b7["text"] = "O"
            self.test = True
        self.test_victory()

    def click_b8(self):
        if self.test:
            self.b8["text"] = "X"
            self.test = False
        else:
            self.b8["text"] = "O"
            self.test = True
        self.test_victory()

    def click_b9(self):
        if self.test:
            self.b9["text"] = "X"
            self.test = False
        else:
            self.b9["text"] = "O"
            self.test = True
        self.test_victory()

    def show_frame(self, frame):
        frame.tkraise()

    def test_victory(self):
        if (self.b1["text"] == self.b2["text"] == self.b3["text"]) and (
            self.b1["text"] != "  "
        ):
            self.show_frame(self.victory)


# Criando objeto de Game
Game(instancia_Tk)

# Loop do game
instancia_Tk.mainloop()
