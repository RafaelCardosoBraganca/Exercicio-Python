#script que leia um nome e diga se há SILVA neles
nome = str(input('qual seu nome: ')).strip().upper()
print('Seu nome tem SILVA? {}'.format('SILVA' in nome))