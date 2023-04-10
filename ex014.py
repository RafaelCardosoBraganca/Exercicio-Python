#escreva um script que leia uma temperatura em celsius
# e converta para Fahrenheit

tc=float(input('Insira uma temperatura em °C: '))
tf= 1.8*tc+32
tk= tc+273.15
print('Você inseriu {:.1f}°C, que equivale à {:.1f}°F'.format(tc, tf))
print('{:.1f}°C Também equivale à {:.1f}K'.format(tc, tk)) #plus
