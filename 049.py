# Pergunta: Leia uma altura e desenhe uma pirâmide centralizada de asteriscos.
# Dica: Diminua os espaços e aumente os asteriscos a cada linha.

altura = int(input('Digite a altura da pirâmide: '))

for i in range(1, altura + 1):
    espacos = altura - i
    asteriscos = 2 * i - 1

    print(' ' * espacos + '*' * asteriscos)