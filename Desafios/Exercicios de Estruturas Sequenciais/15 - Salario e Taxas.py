#Exercicio 15 do site Python Brasil
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.
salarioHora = input("Quanto você ganha por hora? ")
horasTrab = input("Quantas horas trabalha por mês? ")
salarioBruto = float(salarioHora) * float(horasTrab)
impostoRenda = float(salarioBruto) * 0.11
inss = float(salarioBruto) * 0.08
sindicato = float(salarioBruto) * 0.05
salarioLiq = float(salarioBruto) - float(impostoRenda) - float(inss) - float(sindicato)
print("Salario Bruto: R${}\nIR(11%): R${}\nINSS(8%): R${}\nSindicato(5%): R${}\nSalario Liquido: R${}".format(salarioBruto, impostoRenda, inss, sindicato, salarioLiq))
