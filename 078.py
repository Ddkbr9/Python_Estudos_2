# Ordene uma lista de números em ordem crescente sem usar sort() ou sorted().
#
# DICA: compare vizinhos e troque quando estiverem fora de ordem;
# repita até nenhuma troca acontecer.

lista = [5, 2, 8, 1, 3]

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            temp = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = temp

print(lista)