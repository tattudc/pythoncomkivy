dist = float(input("Qual a distância total da viagem? "))
print("Você está perto de começar uma viagem de {} km".format(dist))

if(dist <= 200):
    print("O preço da passagem é {}".format(dist * 0.50))
else:
    print("O preço da sua passagem é {}".format(dist * 0.45))