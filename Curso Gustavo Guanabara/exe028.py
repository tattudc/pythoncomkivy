n1= float(input('Digite sua primeira nota: '))
n2= float(input('Digite a sua segunda note:'))
m1= (n1 + n2)/2

print ('Sua média foi {}'.format(m1))
if m1>=6.00:
    print ('Parabéns você está aprovado')
elif 5.99>=m1>=2.99:
    print('Você está na recuperação')
else:
    print('Você está reprovado')
