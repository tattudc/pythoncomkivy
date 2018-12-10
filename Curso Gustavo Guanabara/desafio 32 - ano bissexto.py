ano = int(input("Digite o ano e saiba se ele é Bissexto: "))
if(ano%4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print("O ano de {} é Bissexto".format(ano))
else:
    print("O ano de {} não é Bissexto".format(ano))