#Exercicio 3.6 do livro de introdução ao algoritimo com Python
#Exercicio de aprovado ou reprovado
Nota1 = float(input("Digite a primeira nota: "))
Nota2 = float(input("Digite a segunda nota: "))
Nota3 = float(input("Digite a terceira nota: "))
ira = (Nota1+Nota2+Nota3)/3
if(Nota1 >= 7.0):
    print("Aprovado na matéria 1!")
else:
    print("Reprovado na matéria 1!")

if(Nota2 >= 7.0):
    print("Aprovado na matéria 2!")
else:
    print("Reprovado na matéria 2!")

if(Nota3 >= 7.0):
    print("Aprovado na matéria 3!")
else:
    print("Reprovado na matéria 3!")

print("O IRA do aluno foi {:.2f}".format(ira))
