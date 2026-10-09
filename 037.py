#Leia um número e imprima sua tabuada do 1 ao 10.
#DICA range(1, 11) — o limite superior nunca entra no laço.

n = int(input('Digite um número: '))

for i in range(1, 11):
    print(n, 'x', i, '=', n * i)