# Pergunta: Crie uma função que aceite qualquer quantidade de
# números e retorne a soma de todos.
# Dica: *args empacota os argumentos em uma tupla que você
# pode percorrer.

def soma(*args):
    total = 0

    for numero in args:
        total += numero

    return total


print(soma(10, 20, 30))
print(soma(5, 8))
print(soma())