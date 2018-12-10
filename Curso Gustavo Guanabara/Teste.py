p1 = input(int("Digite um número: "))

soma = 0
while (p1 > 0):
    soma += p1 % 10
    p1 = int(p1 / 10)
print(soma)
