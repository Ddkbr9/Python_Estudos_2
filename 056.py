# Pergunta: Crie a função titulo(texto), que imprime o texto entre duas linhas de traços.
# Dica: Use len() para descobrir o tamanho do texto e multiplique '-' por esse tamanho.

def titulo(texto):
    linha = '-' * len(texto)

    print(linha)
    print(texto)
    print(linha)


mensagem = input('Digite um título: ')

titulo(mensagem)