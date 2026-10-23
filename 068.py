# Crie uma lista vazia e insira números até o usuário digitar um valor negativo.
# Ao final, exiba a lista.
#
# DICA: o valor que interrompe não deve entrar na lista — teste antes do append().

numeros = []

while True:
    numero = int(input('Digite um número: '))

    if numero < 0:
        break

    numeros.append(numero)

print('Lista:', numeros)