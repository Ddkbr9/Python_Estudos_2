# Pergunta: Leia o peso de 7 pessoas e mostre o maior e o menor peso lidos.
# Dica: Use um for para repetir 7 vezes e compare os pesos.

for i in range(1, 8):
    peso = float(input(f'Digite o peso da {i}ª pessoa: '))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print(f'Maior peso: {maior} kg')
print(f'Menor peso: {menor} kg')