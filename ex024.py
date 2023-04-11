#crie um script que leia um nome da cidade e diga e ela começa com "SANTO"
city = str(input('Digite o nome da cidade: ')).strip()
print(city[:5].upper() == 'SANTO')