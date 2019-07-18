#!/usr/local/bin/python
class Humano:
    #atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalis'
        return self

if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_cavernas()

    print(f'Humano_especie: {Humano.especie}')
    print(f'Humano_especie: {grokn.especie}')
    print(f'Humano_especie: {jose.especie}')

