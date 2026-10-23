# Pergunta: Leia notas até o usuário digitar -1. Mostre a quantidade, a média e quantas notas ficaram acima dela.
# Dica: Use uma lista, sum(), len() e um for para contar as notas acima da média.

notas = []

while True:
    nota = float(input('Digite uma nota (-1 para parar): '))

    if nota == -1:
        break

    notas.append(nota)

if len(notas) > 0:
    media = sum(notas) / len(notas)
    acima = 0

    for nota in notas:
        if nota > media:
            acima += 1

    print(f'Quantidade de notas: {len(notas)}')
    print(f'Média geral: {media:.2f}')
    print(f'Notas acima da média: {acima}')
else:
    print('Nenhuma nota foi informada.')