pessoa = {'Nome' : 'Alberto', 'Idade' : 44, 'Cursos' : ['React', 'Python']}
pessoa['Idade'] = 45
pessoa['Cursos'].append('Angular')
print(pessoa)
pessoa.pop('Idade')
print(pessoa)
pessoa.update({'Idade': 45, 'Sexo' : "M"})
print(pessoa)
del pessoa['Cursos']
print(pessoa)
pessoa.clear()
print(pessoa)