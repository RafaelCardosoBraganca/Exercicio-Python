#escreva um programa que pergunte a quantidade de km percorridos por 
#um carro alugado e também por quantos dias foi alugado, após isso
#calcule o total a pagar, sendo R$ 60/dia alugado e R$0,15/km rodado.

km=float(input('Olá, insira quantos quilômetros foram rodados durante o período de locação: '))
dia=int(input('Por quantos dias o carro ficou alugado? '))
rent= (km*0.15)+(dia*60)
print('O total do aluguel é R${:.2f}'.format(rent))
