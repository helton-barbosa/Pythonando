# Receba um número e mostre todos os números pares de 0 até o número digitado

num = int(input('Entre com um número: '))
contador = 0
while contador <= num:
    if contador % 2 == 0:
        print(f'{contador}')
    contador += 1
