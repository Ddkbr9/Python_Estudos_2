#Crie um jogo de pedra, papel e tesoura contra o computador usando random.randint , exibindo a jogada de cada um e o resultado.
#DICA trate primeiro o caso de empate; sobram só três combinações de vitória para o jogador.


import random
import time

pc = random.randint(1, 3)

j = int(input(''
              '1. Papel\n'
              '2. Tesoura\n'
              '3. Pedra\n'
              'JOKEMPO: '))

time.sleep(1)
print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO')

print('Você escolheu:', j)
print('Computador escolheu:', pc)

if pc == j:
    print('Empate!')
elif (j == 1 and pc == 3) or (j == 2 and pc == 1) or (j == 3 and pc == 2):
    print('Ganhou!')
else:
    print('Perdeu!')