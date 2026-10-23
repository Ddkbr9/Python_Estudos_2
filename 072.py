# Pergunte quantos jogos gerar e sorteie 6 números de 1 a 60 para cada um,
# guardando tudo em uma lista composta.
#
# DICA: random.sample(range(1, 61), 6) já garante números sem repetição.

import random

jogos = []
quantidade = int(input('Quantos jogos? '))

for i in range(quantidade):
    jogos.append(random.sample(range(1, 61), 6))

for jogo in jogos:
    print(sorted(jogo))