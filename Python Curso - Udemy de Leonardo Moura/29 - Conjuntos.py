a = {1, 2, 3}
print(type(a))
a = set('cod3r')
print(a)
a = set('coddd3r')
print('3' in a, '4' not in a)
print({1, 2, 3} == {1, 2, 3, 4})

#operações
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))
print(c1.update(c2))
