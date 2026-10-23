# Pergunta: Liste todos os números perfeitos até 10.000.
# Dica: Some os divisores próprios de cada número e compare a soma com ele mesmo.

for numero in range(2, 10001):
    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma += i

    if soma == numero:
        print(numero)