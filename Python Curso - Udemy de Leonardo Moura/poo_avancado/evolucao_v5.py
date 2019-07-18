#!/usr/local/bin/python
class Humano:
    #atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def inteligente(self):
        raise NotImplementedError('Propriedade não implementada')

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser maior do que zero')
        self._idade = idade

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

    @property
    def inteligente(self):
        return False

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True

if __name__ == '__main__':
    anonimo = Humano('John Doe')

    try:
        print(anonimo.inteligente)
    except NotImplementedError:
        print('Propriedade abstrata')

    jose = HomoSapiens('Jose')
    gronk = Neanderthal('Gronk')
    print('{} da classe {}, inteligente: {}'.format(jose.nome, jose.__class__.__name__, jose.inteligente))
    print('{} da classe {}, inteligente: {}'.format(gronk.nome, gronk.__class__.__name__, gronk.inteligente))