# Crie uma função de Fibonacci recursiva e depois otimize-a guardando
# resultados já calculados. Compare o tempo das duas para n = 35.
#
# DICA: um dicionário como cache transforma a complexidade exponencial
# em linear; time.time() mede a diferença.

import time


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_com_cache(n, memoria):
    if n in memoria:
        return memoria[n]

    if n <= 1:
        return n

    memoria[n] = fibonacci_com_cache(n - 1, memoria) + fibonacci_com_cache(n - 2, memoria)
    return memoria[n]


inicio = time.time()
resultado = fibonacci(35)
tempo_normal = time.time() - inicio

inicio = time.time()
resultado_cache = fibonacci_com_cache(35, {})
tempo_cache = time.time() - inicio

print('Resultado:', resultado)
print('Tempo sem cache:', tempo_normal)
print('Tempo com cache:', tempo_cache)