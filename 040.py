#Leia dois números e mostre todos os pares entre eles.
#DICA o terceiro argumento de range é o passo — ajuste o início para o primeiro par.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i)