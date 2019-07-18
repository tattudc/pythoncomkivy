#!/usr/local/bin/python
class Humano:
    #atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('habilis', 'Erectus', 'Neanderthalis', 'Sapiens')
        return ('Australopiteco',)+ tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

if __name__ == '__main__':
    jose = HomoSapiens('José')
    grokn = Neanderthal('Grokn')

    print(f'Humano_especie: {Humano.especie}')
    print(f'Humano_especie: {grokn.especie}')
    print(f'Humano_especie: {jose.especie}')

