#12 Mais operadores(Membro/Identidade)
lista = [1, 2, 3, 'Ana', 'Carla']
print(2 in lista)
print('Ana' in lista)
print('ana' in lista)
print('Carla' not in lista)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]
print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is lista_c)
