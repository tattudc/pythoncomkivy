class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia #atributos
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}' #retornando em string

d1 = Data(5, 12, 2019) #d1 vira um objeto recebendo a classe Data
print (d1)

d2 = Data(7, 11, 2020)
print(d2)