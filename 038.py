#Calcule e mostre a soma de todos os números de 1 até 100 usando um laço.
#DICA crie um acumulador em zero antes do for e some dentro dele.

soma = 0

for i in range(1, 101):
    soma = soma + i

print('Soma:', soma)