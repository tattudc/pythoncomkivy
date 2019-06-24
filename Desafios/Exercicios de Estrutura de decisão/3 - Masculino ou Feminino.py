#Exercicio 3 do site Python Brasil
#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino,
# M - Masculino, Sexo Inválido.
x1 = str(input("Digite um sexo "))
if x1 == 'm' or x1 == 'M':
    print("Masculino")
elif x1 == 'f' or x1 == 'F':
    print("Feminino")
else:
    print("Sexo invalido")

