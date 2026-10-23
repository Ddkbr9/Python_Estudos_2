# Pergunta: Leia n e mostre os n primeiros termos da sequência de Fibonacci.
# Dica: Comece com a = 0 e b = 1 e atualize os valores a cada repetição.

n = int(input('Quantos termos deseja mostrar? '))

a = 0
b = 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b