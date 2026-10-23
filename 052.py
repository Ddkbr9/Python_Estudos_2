# Pergunta: Crie um jogo da forca com uma palavra sorteada e permita até 6 erros.
# Dica: Use random.choice(), um conjunto para guardar letras e uma variável para contar erros.

import random

palavras = ['python', 'programa', 'computador', 'teclado']
palavra = random.choice(palavras)

letras = set()
erros = 0

while erros < 6:
    exibicao = ''

    for letra in palavra:
        if letra in letras:
            exibicao += letra
        else:
            exibicao += '_'

    print('\nPalavra:', exibicao)
    print(f'Erros: {erros}/6')

    if exibicao == palavra:
        print('Parabéns! Você acertou a palavra!')
        break

    tentativa = input('Digite uma letra: ').lower()

    if len(tentativa) != 1 or not tentativa.isalpha():
        print('Digite apenas uma letra!')
        continue

    if tentativa in letras:
        print('Você já tentou essa letra!')
        continue

    letras.add(tentativa)

    if tentativa not in palavra:
        erros += 1
        print('Letra errada!')

if erros == 6:
    print(f'Você perdeu! A palavra era {palavra}.')