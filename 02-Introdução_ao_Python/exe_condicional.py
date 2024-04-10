# Leia 3 números inteiros e exiba o maior deles

number_1 = input("Entre com o 1º número: ")
number_2 = input("Entre com o 2º número: ")
number_3 = input("Entre com o 3º número: ")

if number_1 > number_2 and number_1 > number_3:
    print(f'{number_1} é o maior.')
elif number_2 > number_1 and number_2 > number_3:
    print(f'{number_2} é o maior.')
else:
    print(f'{number_3} é o maior.')
