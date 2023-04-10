#faça um programa que leia um ângulo qualquer e mostre o valor do sen, cos e tan, desse ângulo

from math import radians, sin, cos, tan
angulo=float(input('Insira o ângulo desejado: '))
sen = sin(radians(angulo))
cosseno = cos(radians(angulo))
tang = tan(radians(angulo))
print('O ângulo {:.0f}° possui seno= {:.2f} ; cosseno = {:.2f} e tangente= {:.2f}'. format(angulo, sen, cosseno, tang))
