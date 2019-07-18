#!/usr/local/bin/python
from datetime import datetime

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def adicionar(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]
        #possível error

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')

def main():
   casa = Projeto('Tarefas de casa')
   casa.adicionar('Passar roupa')
   casa.adicionar('Lavar prato')
   print(casa)

   casa.procurar('Lavar prato').concluir()
   for tarefa in casa.tarefas:
       print(f'-{tarefa}')
   print(casa)

   mercado = Projeto('Compras do mercado')
   mercado.adicionar('Frutas secas')
   mercado.adicionar('Carne')
   mercado.adicionar('Tomate')
   print(mercado)

   comprar_carne = mercado.procurar('Carne')
   comprar_carne.concluir()

   for tarefa in mercado.tarefas:
       print(f'-{tarefa}')

   print(mercado)


if __name__=='__main__':
    main()