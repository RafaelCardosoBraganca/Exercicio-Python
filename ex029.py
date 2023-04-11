#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
print('VELOCIDADE MÁXIMA DA VIA: 80 KM/H')
v = int(input('Qual a velocidade atual do carro: '))
multa = (v-80)*7
if v <= 80:
    print('Boa viagem, dirija com segurança!!')
else:
    print('Você ultrapassou o limite da via em {}Km/h acima do permitido!!! Sua multa será de R${:.2f}'.format(v-80, multa))
