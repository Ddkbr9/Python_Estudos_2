# Pergunta: Leia um número e liste todos os números primos de 2 até ele.
# Dica: Use % para verificar se existe divisão exata e uma variável para identificar os primos.

numero = int(input('Digite um número: '))

for n in range(2, numero + 1):
    primo = True

    for i in range(2, n):
        if n % i == 0:
            primo = False
            break

    if primo:
        print(n, end=' ')