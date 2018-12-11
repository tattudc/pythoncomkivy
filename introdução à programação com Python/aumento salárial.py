#Aumento de salário
#Programa que mostra o salário atual e multiplica pelo seu aumento
salario = float(input("Digite seu salário atual "))
aumento = float(input("Digite quanto vai ser seu aumento "))
calcaumento = salario + ((salario * aumento)/100)
print("-"*20)
print("Seu salário é de R${}".format(salario))
print("O aumento salarial é de {}%".format(aumento))
print("Seu salário com aumento será de R${:.2f}".format(calcaumento))
print("-"*20)
