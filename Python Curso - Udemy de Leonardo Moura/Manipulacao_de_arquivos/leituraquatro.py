#!/usr/local/bin/python
try:
    arquivo = open('pessoa.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:
    print('Finaly')
    arquivo.close()

if arquivo.close:
    print('Arquivo foi fechado')
