#Exercicio 17 do site Python Brasil
#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para
# cima, isto é, considere latas cheias.
metros = input("Digite a quantidade de metros a serem pintadas ")
lata = 18.0 * 6.0
galao = 3.6 * 6.0
qtdLatas = float(metros)/float(lata)
qtdGalao = float(metros)/float(galao)
maiorLata = float(qtdLatas) % 1
maiorGalao = float(qtdGalao) % 1
sobraLata = maiorLata * 18
sobraGalao = float(sobraLata) / 3.6
maiorGalao2 = float(sobraGalao) % 1

if maiorLata >= 0.01:
    qtdLatas = float(qtdLatas) - float(maiorLata)
    qtdLatas = qtdLatas + 1
if maiorGalao >= 0.01:
    qtdGalao = float(qtdGalao) - float(maiorGalao)
    qtdGalao = qtdGalao + 1
if maiorGalao2 >= 0.01:
    sobraGalao = float(sobraGalao) - float(maiorGalao2)
    sobraGalao = sobraGalao + 1

if qtdLatas <= 1: #Lata de 18L
    print("Só será necessário {:.2f} lata e vai custar R${:.2f}".format(qtdLatas, qtdLatas * 80))
else:
    print("Será necessário {:.2f} latas e vai custar R${:.2f}".format(qtdLatas, qtdLatas * 80))

if qtdGalao <= 1: #Galao de 3.6L
    print("Só será necessário {:.2f} lata e vai custar R${:.2f}".format(qtdGalao, qtdGalao * 25))
else:
    print("Será necessário {:.2f} latas e vai custar R${:.2f}".format(qtdGalao, qtdGalao * 25))
print("A melhor compra é {:.0f} Latas a um preço de R${:.2f} e {:.0f} Galões a um preço de R${:.2f} e vai custar no total R${:.2f}".format(qtdLatas, qtdLatas * 80, sobraGalao, sobraGalao * 25, qtdLatas * 80 + sobraGalao * 25))