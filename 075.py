# Leia duas listas de números e mostre os elementos comuns às duas
# e os que existem apenas na primeira.
#
# DICA: percorra a primeira lista testando in na segunda,
# ou converta para set e use & e -.

lista1 = []
lista2 = []

for i in range(int(input('Quantos números na primeira lista? '))):
    lista1.append(int(input('Número: ')))

for i in range(int(input('Quantos números na segunda lista? '))):
    lista2.append(int(input('Número: ')))

comuns = []
so_na_primeira = []

for numero in lista1:
    if numero in lista2 and numero not in comuns:
        comuns.append(numero)
    elif numero not in lista2 and numero not in so_na_primeira:
        so_na_primeira.append(numero)

print('Comuns:', comuns)
print('Só na primeira:', so_na_primeira)