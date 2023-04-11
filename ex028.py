#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
print('O computador pensou em um número inteiro entre 0 e 5')
n = [0 , 1, 2, 3, 4, 5] #Eu sei que existe o randint, porém dessa vez não quis usá-lo
chosen= random.choice(n)
guess = int(input('Adivinhe o número: '))
print('LOADING...')
sleep(3)
if guess==chosen:
    print('Parabéns, você tem o Haki da observação!')
else:
    print('ERRROOUUUU!! ERROU FEIO! ERROU RUDE!')
print('O computador pensou em {} e você palpitou {}!!'.format(chosen, guess))
