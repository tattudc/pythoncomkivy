#Exercicio 16 do site Python Brasil
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
metros = input("Quantos metros será pintada? ")
lata = 18 * 3
qtdLatas = float(metros)/float(lata)
maiorLata = float(qtdLatas) % 1
if maiorLata >= 0.01:
    qtdLatas = float(qtdLatas) - float(maiorLata)
    qtdLatas = qtdLatas + 1
if qtdLatas <= 1:
    print("Só será necessário {:.2f} lata e vai custar R${:.2f}".format(qtdLatas, qtdLatas * 80))
else:
    print("Será necessário {:.2f} latas e vai custar R${:.2f}".format(qtdLatas, qtdLatas * 80))
