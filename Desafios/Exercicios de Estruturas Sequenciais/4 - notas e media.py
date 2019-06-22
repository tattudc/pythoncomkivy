#Exercicio 4 do site Python Brasil
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = [0, 0, 0, 0]
notas[0] = int(input("Digite uma nota"))
notas[1] = int(input("Digite outra nota"))
notas[2] = int(input("Digite a terceira nota"))
notas[3] = int(input("Digite a quarta nota"))
media = (notas[0] + notas[1] + notas[2] + notas[3])/4
print("A média do aluno e igual a {}".format(media))
