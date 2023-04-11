#crie um script que leia um número de 1 a 9999 e mostre as unidades, dezenas, centenas e milhares

n = int(input('Insira um número(máx 4 dígitos): '))
print('Analisando', n)
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print ('Unidade:', u)
print('Dezena:', d)
print('Centena:', c)
print('Milhar:', m)
