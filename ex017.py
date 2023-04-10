#calculando a hipotenusa porém de forma simplificada
from math import hypot
co= float(input('Comprimento do catato oposto: '))
ca= float(input('Comprimento do cateto adjacente: '))
hi= hypot(co, ca)
print('o comprimento da hipotenusa é {:.2f}'.format(hi))