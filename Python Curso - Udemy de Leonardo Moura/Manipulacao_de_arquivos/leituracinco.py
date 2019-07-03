#!/usr/local/bin/python
with open('pessoa.csv') as arquivo:
    with open('pessoa.txt', 'w') as saida: 
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file = saida)
if arquivo.close:
    print('Arquivo foi fechado')
if saida.close:
    print('Arquivo saida foi fechado')
