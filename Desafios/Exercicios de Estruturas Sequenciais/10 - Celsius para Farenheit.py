#Exercicio 10 do site Python Brasil
#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
#Formula => tf = (tc * (9/5)) + 32
tc = input("Digite uma temperatura em graus celsius ")
tf = (float(tc) * (9/5)) + 32
print("A conversao de {}ºC e igual a {:.0f}ºF".format(tc, tf))