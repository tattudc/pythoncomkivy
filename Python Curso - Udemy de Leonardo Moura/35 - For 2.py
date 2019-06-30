palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end= ', ')
print('FIM')

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

diasDaSemana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado')
for dia in diasDaSemana:
    print(f'Hoje é dia {dia}')

for letra in set('Muito Legal'):
    print(letra)

