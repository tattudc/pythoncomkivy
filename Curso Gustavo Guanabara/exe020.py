import random
nam1= str(input('Digite um nome'))
nam2= str(input('Digite outro nome'))
nam3= str(input('Digite o terceiro nome'))
nam4= str(input('Digite o quarto nome'))
list= [nam1,nam2,nam3,nam4]
random.shuffle(list)

print ('A ordem de apresentação será ')
print (list)
