from tkinter import *

class application():
    def __init__(self, master = None):
        self.fontepadrao = ("Arial", "10") #fonte geral

        self.primeiroContainer = Frame(master) #primeiro container
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundocontainer = Frame(master)  # segundo container
        self.segundocontainer["padx"] = 100
        self.segundocontainer["pady"] = 20
        self.segundocontainer.pack()

        self.terceirocontainer = Frame(master)  # terceiro container
        self.terceirocontainer["padx"] = 100
        self.terceirocontainer["pady"] = 20
        self.terceirocontainer.pack()

        self.titulo = Label(self.primeiroContainer, text = "TELA INICIO")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomebotao = Button(self.segundocontainer, text="CADASTRAR\nVENDEDOR", background = 'red', font=self.fontepadrao, height = 10, width = 30)
        self.nomebotao.pack(side=LEFT)

        self.nomeLabel = Label(self.segundocontainer, text="   ", font=self.fontepadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nomebotao2 = Button(self.segundocontainer, text="CADASTRAR\nPRODUTOS", background = 'green', font=self.fontepadrao, height = 10, width = 30)
        self.nomebotao2.pack(side=LEFT)

        self.nomebotao3 = Button(self.terceirocontainer, text="CADASTRAR\nCLIENTE", background='blue', font=self.fontepadrao, height = 10, width = 30)
        self.nomebotao3.pack(side=LEFT)

        self.nomeLabel2 = Label(self.terceirocontainer, text="   ", font=self.fontepadrao)
        self.nomeLabel2.pack(side=LEFT)

        self.nomebotao4 = Button(self.terceirocontainer, text="REALIZAR\nVENDA", background='yellow', font=self.fontepadrao, height = 10, width = 30)
        self.nomebotao4.pack(side=LEFT)


root = Tk()
application(root)
root.title("SISTEMA DE LOJA 0.1")
root.geometry('800x500')
root.mainloop()