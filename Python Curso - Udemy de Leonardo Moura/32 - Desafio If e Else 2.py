def faixaEtaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 64):
        return  'Adulto'
    elif idade in range(64, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade inválida'

if __name__ == '__main__':
    for idade in (17, 0, 33, 87, 103, -2):
        print(f'{idade}: {faixaEtaria(idade)}')

