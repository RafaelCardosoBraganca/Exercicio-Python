#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

d=int(input('Qual a distância da sua viagem? '))
dc= d*(1/2)
dl= d*0.45
if d < 200:
    print('Sua viagem é de {}km, o preço de sua passagem será R${:.2f}'.format(d, dc))
else:
    print('Sua viagem é de {}km, o preço de sua passagem será R${:.2f}'.format(d, dl))

