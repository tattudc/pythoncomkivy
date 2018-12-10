import math
ang1= float(input('Digite o angulo que você deseja: '))
sen1= math.sin(math.radians(ang1))
cos1= math.cos(math.radians(ang1))
tan1= math.tan(math.radians(ang1))

print ('O seno de {} é {:.3f}'.format(ang1,sen1))
print ('O Coseno de {} é {:.3f}'.format(ang1,cos1))
print ('A tangente de {} é {:.3f}'.format(ang1,tan1))
