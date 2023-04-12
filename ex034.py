#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário: '))
if salario > 1250:
    aumento = salario*0.1 + salario
    print('Seu aumento foi de 10%! Seu salário será R${:.2f}'.format(aumento))
else:
    aumento = salario*0.15 + salario
    print('Seu aumento foi de 15%! Seu salário será R${:.2f}'.format(aumento))
