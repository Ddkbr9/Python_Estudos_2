# Leia vários números e mostre a lista sem valores repetidos,
# preservando a ordem de entrada.
#
# DICA: só adicione se o valor ainda não estiver na lista (if x not in lista).

numeros = []
unicos = []

quantidade = int(input('Quantos números? '))

for i in range(quantidade):
    numero = int(input('Número: '))
    numeros.append(numero)

    if numero not in unicos:
        unicos.append(numero)

print(unicos)