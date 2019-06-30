def conceitoNota(y):
    x = float(y)
    if x <= 10 and x >= 9.1:
        return 'Conceito A'
    elif x <= 9.0 and x >= 8.1:
        return 'Conceito A-'
    elif x <= 8.0 and x >= 7.1:
        return 'Conceito B'
    elif x <= 7.0 and x >= 6.1:
        return 'Conceito B-'
    elif x <= 6.0 and x >= 5.1:
        return 'Conceito C'
    elif x <= 5.0 and x >= 4.1:
        return 'Conceito C-'
    elif x <= 4.0 and x >= 3.1:
        return 'Conceito D'
    elif x <= 3.0 and x >= 2.1:
        return 'Conceito D-'
    elif x <= 2.0 and x >= 1.1:
        return 'Conceito E'
    elif x <= 1.0 and x >= 0.0:
        return 'Conceito E-'
    else:
        return 'Nota invalida'

if __name__ == '__main__':
    valor_informado = input('Nota Aluno: ')
    conceito = conceitoNota(valor_informado)
    print(conceito)
