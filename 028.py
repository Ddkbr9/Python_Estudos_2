#Leia três números e mostre qual é o maior, sem usar a função max() .
#DICA compare o primeiro com o segundo, guarde o vencedor e compare com o terceiro.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

maior = a

if b > maior:
    maior = b

if c > maior:
    maior = c

print('Maior número:', maior)