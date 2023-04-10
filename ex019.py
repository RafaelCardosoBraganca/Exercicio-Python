#crie um script que leia 4 srtings e 'sorteie' uma das 4 inseridas
# irei fazer um script que sorteie 4 alunos, e mostre o sorteado
from random import choice
n1= str(input('O Primeiro Aluno  :   '))
n2= str(input('O Segundo Aluno   :   '))
n3= str(input('O Terceiro Aluno  :   '))
n4= str(input('O Quarto Aluno    :   '))
lista= [n1, n2, n3, n4]
chosenOne= choice(lista)
print('='*40)
print('O escolhido foi... {}!!'.format(chosenOne))
