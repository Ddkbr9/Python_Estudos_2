# Pergunta: Crie a função maior(), que recebe 5 parâmetros e retorna o maior deles.
# Dica: Comece pelo primeiro número e compare os outros com o maior valor atual.

def maior(a, b, c, d, e):
    resultado = a

    if b > resultado:
        resultado = b
    if c > resultado:
        resultado = c
    if d > resultado:
        resultado = d
    if e > resultado:
        resultado = e

    return resultado


n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
n4 = float(input('Digite o quarto número: '))
n5 = float(input('Digite o quinto número: '))

print(f'O maior número é {maior(n1, n2, n3, n4, n5)}')