#Exercicio 7 do site Python Brasil
#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado1 = int(input("Digite o lado do quadrado "))
lado2 = int(input("Digite o outro lado do quadrado "))
area = lado1 * lado2
dobro = area * 2
print("A area do quadrado e de {} e seu dobro e {}".format(area, dobro))
