# Leia uma lista e um número k; devolva a lista rotacionada k posições
# à direita.
# Exemplo: [1, 2, 3, 4, 5] com k = 2 → [4, 5, 1, 2, 3].
#
# DICA: fatiamento resolve em uma linha: junte lista[-k:] com lista[:-k].

lista = []

quantidade = int(input('Quantos números terá a lista? '))

for i in range(quantidade):
    numero = int(input('Digite um número: '))
    lista.append(numero)

k = int(input('Quantas posições rotacionar? '))
k = k % len(lista)

if k > 0:
    lista = lista[-k:] + lista[:-k]

print('Lista rotacionada:', lista)