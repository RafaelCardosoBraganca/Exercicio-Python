#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas 
#e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Insira o primeiro lado: '))
b = float(input('Insira o segundo lado: '))
c = float(input('Insira o terceiro lado: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Não é um triângulo!')
elif (a == b ) and (a == c):
    print('É um triângulo equilátero!')
elif (a == b) or (a == c) or (b == c):
    print('é um triângulo isóceles!')
else:
    (print('é um triângulo escaleno!'))
#fiz um plus e não apenas informei qual formaria, ou não, um triângulo, como fiz com que informasse o tipo de triângulo

