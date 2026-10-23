# Pergunta: Crie leia_int(mensagem) que insiste até o usuário
# digitar um número inteiro válido, e só então retorna o valor.
# Dica: Use while True com .isdigit() ou try/except antes
# do return.

def leia_int(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print('Erro! Digite um número inteiro válido.')


numero = leia_int('Digite um número inteiro: ')
print(f'Você digitou o número {numero}.')