#Exercicio 12 do site Python Brasil
#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula: (72.7*altura) - 58
altura = input("Digite sua altura ")
pesoIdeal = (72.7 * float(altura)) - 58
print("O seu peso ideal é {}kgs".format(pesoIdeal))
