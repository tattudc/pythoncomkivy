#Ano bissexto
ano = int(input("Ano? "))
if (ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0)):
          print("Bissexto")
else:
          print("Nao Bissexto")
