# Leia vários números do usuário, guarde em uma lista e exiba apenas os ímpares.
#
# DICA: percorra a lista já preenchida e filtre com % 2.

numeros = []

quantidade = int(input('Quantos números você quer digitar? '))

for i in range(quantidade):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

print('Números ímpares:')

for numero in numeros:
    if numero % 2 != 0:
        print(numero)