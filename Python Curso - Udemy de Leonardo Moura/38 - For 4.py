from random import randint
def sortearDados():
    return randint(1, 6)

for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortearDados() == i:
        print("ACERTOU!!", i)
        break
else:
    print("Não acertou o numero")