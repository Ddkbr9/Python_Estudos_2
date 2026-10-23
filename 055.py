# Pergunta: Crie a função media(), que recebe 5 parâmetros e retorna a média.
# Dica: Some os valores e divida por 5. Use return para devolver o resultado.

def media(a, b, c, d, e):
    resultado = (a + b + c + d + e) / 5
    return resultado


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
n5 = float(input('Digite a quinta nota: '))

print(f'A média é {media(n1, n2, n3, n4, n5):.2f}')