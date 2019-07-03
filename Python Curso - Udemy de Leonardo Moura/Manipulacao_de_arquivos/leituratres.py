#!/usr/local/bin/python
arquivo = open('pessoa.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()
