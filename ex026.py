#faça um script que leia uma frase e diga:
#1- quantas vezes a letra A aparece
#2- em que posição ela aparece pela primeira vez
#3- em que posição ela aparece por último

f = str(input('Escreva uma frase: ')).strip().upper().replace('Á', 'A').replace('Ã', 'A').replace('À','A').replace('Â', 'A')
a = f.count('A')
posicaoA = f.find('A')
print('A Letra A apareceu ao todo {} vezes'.format(a))
print('A letra A apareceu primeiro na posição:', posicaoA)
print('A letra A apareceu por último na posição: {}'.format(f.rfind('A')))

