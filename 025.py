#Leia um número e informe se ele é par ou ímpar.
#DICA o resto da divisão por 2 ( n % 2 ) só pode ser 0 ou 1.

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('Par')
else:
    print('Ímpar')