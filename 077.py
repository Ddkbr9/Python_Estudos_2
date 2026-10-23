# Leia 9 números para preencher uma matriz 3×3 e mostre a soma de cada
# coluna, a soma da segunda linha e o maior valor da terceira coluna.
#
# DICA: use laços aninhados; matriz[linha][coluna] acessa cada célula.

matriz = []

for linha in range(3):
    atual = []
    for coluna in range(3):
        atual.append(int(input('Digite um número: ')))
    matriz.append(atual)

for coluna in range(3):
    print('Soma da coluna:', sum(matriz[linha][coluna] for linha in range(3)))

print('Soma da segunda linha:', sum(matriz[1]))
print('Maior da terceira coluna:', max(matriz[linha][2] for linha in range(3)))