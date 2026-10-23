# Pergunta: Sorteie um número de 1 a 10 e peça palpites até o usuário acertar.
# Dica: Use random.randint(), while e uma variável para contar as tentativas.

import random

numero = random.randint(1, 10)
tentativas = 0
palpite = 0

while palpite != numero:
    palpite = int(input('Adivinhe o número de 1 a 10: '))
    tentativas += 1

    if palpite != numero:
        print('Você errou! Tente novamente.')

print(f'Você acertou em {tentativas} tentativas!')