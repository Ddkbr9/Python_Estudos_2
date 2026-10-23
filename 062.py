# Escreva uma função recursiva que calcula o fatorial de um número.
#
# DICA: o caso base é n <= 1 retornando 1 — sem ele a recursão nunca para.

def fatorial(n):
    if n <= 1:
        return 1

    return n * fatorial(n - 1)


numero = int(input('Digite um número: '))
print(fatorial(numero))