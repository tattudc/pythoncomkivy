#Exercicio 9 do site Python Brasil
#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9).
faren = input("Digite uma temperatura em Farenheit ")
cel = (5 * (int(faren) - 32) /9)
print("{:.2f} graus celsius".format(cel))
