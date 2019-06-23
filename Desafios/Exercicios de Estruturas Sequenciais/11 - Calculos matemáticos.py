#Exercicio 11 do site Python Brasil
#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
x1 = input("Insira um numero inteiro ")
x2 = input("Insira outro numero inteiro")
x3 = input("Insira um numero decimal ")

calc1 = (int(x1) * 2) + (int(x2) / 2)
calc2 = (float(x1) * 3) + float(x3)
calc3 = float(x3) ** 3
print("O primeiro calculo da {}, o segundo da {}, e o terceiro da {}".format(calc1, calc2, calc3))