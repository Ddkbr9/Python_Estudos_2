# Crie duas listas com 5 números cada e exiba a soma dos elementos correspondentes.
#
# [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1] → [6, 6, 6, 6, 6].
#
# DICA: percorra os índices com range(len(lista)) e some as duas posições.

lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 4, 3, 2, 1]
somas = []

for i in range(len(lista1)):
    somas.append(lista1[i] + lista2[i])

print(somas)