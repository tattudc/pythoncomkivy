#Exercicio 13 do site Python Brasil
#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
altura = input("Digite sua altura ")
pesoIdealHomem = (72.7 * float(altura)) - 58
pesoIdealMulher = (62.1 * float(altura)) - 44.7
print("De acordo com sua altura seu peso ideal se for Homem é {:.2f}kgs e se for Mulher é {:.2f}kgs".format(pesoIdealHomem, pesoIdealMulher))