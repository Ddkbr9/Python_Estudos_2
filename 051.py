# Pergunta: Converta um número decimal para binário sem usar bin().
# Dica: Divida por 2, guarde os restos e coloque cada novo resto no início da string.

numero = int(input('Digite um número decimal: '))

if numero == 0:
    binario = '0'
else:
    binario = ''

    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero = numero // 2

print(f'Número em binário: {binario}')