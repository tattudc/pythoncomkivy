#Exercicio 14 do site Python Brasil
#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
#(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
#variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
#e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
pesoPeixe = input("Insira o peso do peixe ")
excesso = float(pesoPeixe) - 50
multa = float(excesso) * 4
if excesso <= 0:
    print("Não vai pagar multa")
else:
    print("O valor do excesso foi de {:.2f} kgs e a multa a pagar é de R$ {:.2f}".format(excesso, multa))