#Exercicios do Livro Introdução ao Algoritmo com Python
#Exercicio 3.7
#Calcular 2 números inteiros e imprimir na tela o resultado
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
result = num1 + num2
print(result)
print("-=-"*15)
#Exercicio 3.8
#Criar um programa que leia a medida em metros e mostre em mm
metros1 = float(input("Digite uma medida em metros: "))
milimetros = metros1 * 1000
print("A medida em metros digitada foi de {} m, que em milimetros dá {} mm".format(metros1, milimetros))
print("-=-"*15)
#Exercicio 3.9
#Crie um programa que transforme os dias, horas, minutos e segundos do usuário
#em segundos
dias = int(input("Digite uma quantidade de dias: "))
horas = int(input("Digite uma quantidade de horas: "))
minutos = int(input("Digite uma quantidade de minutos: "))
segundos = int(input("Digite uma quantidade de segundos: "))
calc = segundos + (minutos * 60 + ( horas * 3600 + ( dias * 86400)))
print("A quantidade de segundos total é de {} segundos".format(calc))
