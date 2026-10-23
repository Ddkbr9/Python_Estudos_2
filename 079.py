# Implemente a busca binária em uma lista ordenada e informe a posição
# do valor procurado (ou -1 se não existir).
#
# DICA: mantenha os ponteiros inicio e fim e descarte metade do intervalo
# a cada iteração.

lista = [1, 3, 5, 7, 9]
valor = int(input('Procurar: '))
inicio = 0
fim = len(lista) - 1
posicao = -1

while inicio <= fim:
    meio = (inicio + fim) // 2

    if lista[meio] == valor:
        posicao = meio
        break
    elif lista[meio] < valor:
        inicio = meio + 1
    else:
        fim = meio - 1

print(posicao)