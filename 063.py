# Escreva uma função recursiva que imprima os movimentos necessários
# para mover N discos entre três pinos.
#
# DICA: mova N-1 discos para o pino auxiliar, mova o maior para o destino
# e repita a lógica.

def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print('Mover disco de', origem, 'para', destino)
    else:
        hanoi(n - 1, origem, auxiliar, destino)
        print('Mover disco de', origem, 'para', destino)
        hanoi(n - 1, auxiliar, destino, origem)


quantidade = int(input('Digite a quantidade de discos: '))
hanoi(quantidade, 'A', 'C', 'B')